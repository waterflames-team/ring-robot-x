import model.config
import model.logger
import importlib
import os
import traceback
import json
import sys


def import_func(path):
    return importlib.import_module(path)

def firstload():
    model.logger.moduleLoggerMain.info("[RingRobotX] 正在初始化（一般情况下，你可以通过 ctrl+c 的方式终止此进程，但是下次使用时仍会开始初始化）")
    path = os.getcwd() + "/func_packages/"
    name = os.path.basename(path)

    func_enabled_packages = []

    mypath = os.listdir(r'' + path)
    mypath.sort()
    status=False

    for i in mypath:
        if os.path.isdir(path + "/" + i) and i != "__pycache__":
            try:
                file_obj = open(path + "/" + i + "/config.json")
                jso = json.loads(file_obj.read())
                if jso["enable"] and jso["need_first_load"]:
                    pack = import_func("func_packages." + i + ".setup")
                    pack.setup()
                    status=True
            except:
                print("[本地] 初始化技能失败，忽略：" + i)
                traceback.print_exc()
                pass
        else:
            continue
    now["first_load"] = False
    pathn = model.config.APPConfig()
    pathn.setModelName("api-version")
    pathn.setConfig(json.dumps(now))
    return status

status=firstload()
if status:
    model.logger.moduleLoggerMain.info("[RingRobotX] 初始化完成！正在重载程序......")
    os.execl(sys.executable, sys.executable, *sys.argv)
model.logger.moduleLoggerMain.info("[RingRobotX] 初始化完成！没有需要初始化的技能，不需要重载。")