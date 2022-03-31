import importlib
import json
import os
import time

import model.config
import model.tts
import model.logger
import model.hook

def run_tts(string, ttsexec):
    # TODO 这里的todo是为了引起你的注意。
    # 这里可以添加你自定义的tts服务
    # 如果你希望系统默认使用某一种tts服务，请修改run函数的参数之一”ttsexec“修改为你想使用的tts服务
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
    path1 = path1["funcpack_path"]

    module_logfile = "./log/main-Func-" + time.strftime("%Y%m%d") + '.log'
    moduleLogger = model.logger.AppLogger("RingRobotX-Core-Func", module_logfile)
    moduleLogger.info("Function load... String:" + string)

    if (path.getConfig()["is_updown"] == True):  # 连续对话被定义
        file = path.getConfig()["updown_funcname"]  # 获取连续对话重定向函数名
        package = importlib.import_module(".main", package=path1 + "." + file)
        returncon = package.main(string, True)# 传入true，因为if语句判定为true
        run_tts(returncon['string'], ttsexec)
        moduleLogger.info("Package running" + json.dumps(returncon))
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
        moduleLogger.info("Function end.")
        model.hook.runhook_fast("RRCore.Model.After.FuncRunning", {"string": string, "ttsexec": ttsexec})
        return run_tts(returncon['string'], ttsexec)

    if os.path.exists(path1) == False:
        moduleLogger.error('this path not exist')
        moduleLogger.info("Function end.")
        return
    files = os.listdir(path1)

    for file in files:  # 遍历所有技能包
        if os.path.isdir(os.path.join(path1, file)):

            if os.path.exists(os.path.join(path1, file) + '/config.json') == False | os.path.exists(
                    os.path.join(path1, file) + '/main.py') == False:
                continue  # 技能包文件夹内无config和main

            with open(os.path.join(path1, file) + '/config.json') as file_obj:
                contents = file_obj.read()
                contents = json.loads(contents)
                if (contents['enable'] == True and contents['funcType'] == "Func" ):  # 技能包启用
                    package = importlib.import_module(".main", package=path1 + "." + file)
                    if package.check(string) == True:  # 技能包觉得我可以
                        moduleLogger.info("Found package:" + file)
                        returncon = package.main(string, False) #传入false，因为如果true了话早在前面true了
                        moduleLogger.info("Package running" + json.dumps(returncon))
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

                        moduleLogger.info("Function end.")
                        model.hook.runhook_fast("RRCore.Model.After.FuncRunning",
                                                {"string": string, "ttsexec": ttsexec})
                        return run_tts(returncon['string'], ttsexec)
