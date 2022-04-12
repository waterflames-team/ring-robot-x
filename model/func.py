import importlib
import json
import os
import time

import model.config
import model.tts
import model.logger
import model.hook
from func_packages import func_packages_class


def run_tts(string, ttsexec):
    if ttsexec == "tts":
        model.tts.tts(string)
    elif ttsexec == "print":
        print(string)
    elif ttsexec == "return":
        return string
    return


def run(string, ttsexec="tts"):

    model.hook.runhook_fast("RRCore.Model.Before.FuncRunning", {"string":string,"ttsexec":ttsexec})

    path = model.config.APPConfig()
    path.setModelName("func")
    path1 = path.getConfig()
    path1 = "func_packages"
    model_class= func_packages_class

    module_logfile = "./log/main-Func-" + time.strftime("%Y%m%d") + '.log'
    moduleLogger = model.logger.AppLogger("RingRobotX-Core-Func", module_logfile)
    moduleLogger.info("Function load... String:" + string)

    if (path.getConfig()["is_updown"] == True):  # 连续对话被定义
        file = path.getConfig()["updown_funcname"]  # 获取连续对话重定向函数名
        package = model_class[file]
        try:
            returncon = package.main(string, True)# 传入true，因为if语句判定为true
        except:
            moduleLogger.error('连续对话被开启，但是因为某些原因无法完成。可能是因为连续对话开启时技能被移除。请尝试编辑config/func.json，将is_updown值改为false')
            run_tts("哎呀，连续对话失败了呢。", ttsexec)

            # TODO 这里的todo是为了引起你的注意。
            # 如果你在调试连续对话时，可以将下面的注释掉

            origin_con = path.getConfig()
            origin_con['is_updown'] = False
            origin_con['updown_funcname'] = ""
            path.setConfig(json.dumps(origin_con))

            return

        moduleLogger.info("连续对话技能包：" + file)
        run_tts(returncon['string'], ttsexec)
        moduleLogger.info("获得答复：：" + json.dumps(returncon))
        if (returncon['return'] == 1):  # 继续连续对话
            origin_con = path.getConfig()
            origin_con['is_updown'] = True
            origin_con['updown_funcname'] = file
            path.setConfig(json.dumps(origin_con))
            model.hook.runhook_fast("RRCore.Model.After.ContinueEnable", {"string": string, "ttsexec": ttsexec})
        else:  # 取消连续对话模式
            origin_con = path.getConfig()
            origin_con['is_updown'] = False
            origin_con['updown_funcname'] = ""
            path.setConfig(json.dumps(origin_con))
            model.hook.runhook_fast("RRCore.Model.After.ContinueDisable", {"string": string, "ttsexec": ttsexec})
        func_packages_class[file]=package
        moduleLogger.info("运行完毕")
        model.hook.runhook_fast("RRCore.Model.After.FuncRunning", {"string": string, "ttsexec": ttsexec})
        return run_tts(returncon['string'], ttsexec)

    if os.path.exists(path1) == False:
        moduleLogger.error('报告：但是没有找到相应的技能文件夹，请检查')
        moduleLogger.info("运行完毕")
        return
    files = os.listdir(path1)

    for file in files:  # 遍历所有技能包
        if os.path.isdir(os.path.join(path1, file)):

            if os.path.exists(os.path.join(path1, file) + '/config.json') == False | os.path.exists(
                    os.path.join(path1, file) + '/main.py') == False:
                continue  # 技能包文件夹内无config和main

            with open(os.path.join(path1, file) + '/config.json') as file_obj: # 打开config
                contents = file_obj.read()
                contents = json.loads(contents)
                if (contents['enable'] == True and contents['funcType'] == "Func" ):  # 技能包启用
                    package = model_class[file] # 获取技能包class
                    if package.check(string) == True:  # 技能包觉得我可以
                        moduleLogger.info("技能运行：" + file)
                        returncon = package.main(string, False) #传入false，因为如果true了话早在前面true了
                        moduleLogger.info("获得答复：" + json.dumps(returncon))
                        if (returncon['return'] == 1):  # 连续对话启用
                            origin_con = path.getConfig()
                            origin_con['is_updown'] = True
                            origin_con['updown_funcname'] = file
                            path.setConfig(json.dumps(origin_con))

                            model.hook.runhook_fast("RRCore.Model.After.ContinueEnable",
                                                    {"string": string, "ttsexec": ttsexec})

                        else:  # 无连续对话
                            origin_con = path.getConfig()
                            origin_con['is_updown'] = False
                            origin_con['updown_funcname'] = ""
                            path.setConfig(json.dumps(origin_con))

                            model.hook.runhook_fast("RRCore.Model.After.ContinueDisable",
                                                    {"string": string, "ttsexec": ttsexec})
                        func_packages_class[file] = package # 用完的class放回去，不然会玄学
                        moduleLogger.info("技能运行完毕！")
                        model.hook.runhook_fast("RRCore.Model.After.FuncRunning",
                                                {"string": string, "ttsexec": ttsexec})
                        return run_tts(returncon['string'], ttsexec)
