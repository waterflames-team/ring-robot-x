import model.config
import model.logger
import importlib
import os
import traceback
import json
import sys


def import_func(path):
    return importlib.import_module(path)

now=model.config.fastGetConfig("api-version")
if now["first_load"]:
    path = os.getcwd() + "/func_packages/"
    name = os.path.basename(path)

    func_enabled_packages = []


    mypath = os.listdir(r'' + path)
    mypath.sort()

    for i in mypath:
        if os.path.isdir(path + "/" + i) and i != "__pycache__":
            try:
                pack = import_func("func_packages." + i + ".setup")
                pack.setup()
            except:
                print("[本地] 初始化技能失败，忽略：" + i)
                traceback.print_exc()
                pass
        else:
            continue
    now["first_load"]=False
    pathn = model.config.APPConfig()
    pathn.setModelName("api-version")
    pathn.setConfig(json.dumps(now))
    model.logger.moduleLoggerMain.info("[RingRobotX] 初始化完成！正在重载程序......")
    os.execl(sys.executable, sys.executable, *sys.argv)