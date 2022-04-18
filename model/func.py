import json
import os
import time

import model.config
import model.tts
import model.logger
import model.hook
import model.check
from func_packages import func_packages_class


def run_tts(string, ttsexec):
    if ttsexec == "tts":
        model.tts.tts(string)
    elif ttsexec == "print":
        print(string)
    elif ttsexec == "return":
        return string
    return


module_logfile = "./log/main-Func-" + time.strftime("%Y%m%d") + '.log'
moduleLogger = model.logger.AppLogger("RingRobotX-Core-Func", module_logfile)

pathn = model.config.APPConfig()
pathn.setModelName("func")
pathn=path.getConfig()


def set_updown(status, path, file):
    origin_con = path.getConfig()
    origin_con['is_updown'] = status
    origin_con['updown_funcname'] = file
    path.setConfig(json.dumps(origin_con))


def run_funcpack(package, string, ttsexec, path, file):
    moduleLogger.info("技能运行：" + file)
    returncon = package.main(string, False)  # 传入false，因为如果true了话早在前面true了
    moduleLogger.info("获得答复：" + json.dumps(returncon))
    if returncon["return"] == 1:
        set_updown(True, path, file)
        model.hook.runhook_fast("RRCore.Model.After.ContinueEnable",
                                {"string": string, "ttsexec": ttsexec})
    else:
        set_updown(False, path, file)
        model.hook.runhook_fast("RRCore.Model.After.ContinueDisable",
                                {"string": string, "ttsexec": ttsexec})

    func_packages_class[file] = package  # 用完的class放回去，不然会玄学
    moduleLogger.info("技能运行完毕！")
    model.hook.runhook_fast("RRCore.Model.After.FuncRunning",
                            {"string": string, "ttsexec": ttsexec})
    return run_tts(returncon['string'], ttsexec)

def run(string, ttsexec="tts"):
    model.hook.runhook_fast("RRCore.Model.Before.FuncRunning", {"string": string, "ttsexec": ttsexec})

    moduleLogger.info("技能运行，输入：" + string)

    '''
    path = model.config.APPConfig()
    path.setModelName("func")
    '''
    path1 = "func_packages"
    model_class = func_packages_class

    if pathn.getConfig()["is_updown"]:  # 连续对话被定义
        file = pathn.getConfig()["updown_funcname"]  # 获取连续对话重定向函数名
        package = model_class[file]
        try:
            run_funcpack(package, string, ttsexec, pathn, file)  # 运行
        except:
            moduleLogger.error('连续对话被开启，但是因为某些原因无法完成。可能是因为连续对话开启时技能被移除。请尝试编辑config/func.json，将is_updown值改为false')
            run_tts("哎呀，连续对话失败了呢。", ttsexec)

            # TODO 这里的todo是为了引起你的注意。
            # 如果你在调试连续对话时，可以将下面的注释掉

            traceback.print_exc()

            set_updown(False, path, file)  # 更改连续对话状态

            return

    if not os.path.exists(path1):
        moduleLogger.error('报告：没有找到相应的技能文件夹，请检查')
        moduleLogger.info("运行完毕")
        return
    files = os.listdir(path1)

    for file in files:  # 遍历所有技能包
        if os.path.isdir(os.path.join(path1, file)):

            if not model.check.check_FuncFilePath(path1, file):
                continue  # 技能包文件夹内无config和main

            # print(model_class)

            package = model_class[file]  # 获取技能包class
            if package.check(string):  # 技能包觉得我可以
                run_funcpack(package, string, ttsexec, pathn, file)

if pathn["funcEnable"]:
    model.hook.add_hook_fast("RRCore.Model.FuncAction", run)
