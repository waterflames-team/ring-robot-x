clas = {}
import importlib
import json
import os
    # 模块化自动引入
import traceback

print("[本地] 正在加载技能包")

path = os.path.dirname(__file__)
name = os.path.basename(path)

def import_func(path):
    return importlib.import_module(path)

for i in os.listdir(r'' + path):
    if os.path.isdir(path + "/" + i) and i != "__pycache__":
        try:
            file_obj = open(path + "/" + i + "/config.json")
            jso=json.loads(file_obj.read())
            if jso["enable"]:
                pack = import_func(name + '.' + i + ".main")
                if jso["funcType"] == "Func":
                    clas[i] = getattr(pack, "Main")()
                #print(i)
            else:
                print("[本地] 技能包禁用，忽略：" + i)
        except:
            print("[本地] 加载技能包失败，忽略：" + i)
            traceback.print_exc()
            pass
    else:
        continue

func_packages_class = clas