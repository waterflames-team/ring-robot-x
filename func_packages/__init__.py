# -*- coding: utf-8 -*-
import importlib
import json
import os
#模块化自动引入
import traceback

print("[本地] 正在加载技能包")

path = os.path.dirname(__file__)
name = os.path.basename(path)

'''

for _, file, _ in pkgutil.iter_modules([path]):
    try:
        importlib.import_module(name+'.'+file)
        print("[本地] 成功加载技能包："+file)
    except:
        print("[本地] 加载技能包失败，忽略：" + file)
        pass
'''

def import_func(path):
    importlib.import_module(path)

for i in os.listdir(r''+path):
    if os.path.isdir(path+"/"+i) and i!="__pycache__":
        try:
            file_obj = open(path+"/"+i+"/config.json")
            if json.loads(file_obj.read())["enable"]:
                import_func(name + '.' + i + ".main")
                print("[本地] 成功加载技能包：" + i)
            else:
                print("[本地] 技能包禁用，忽略：" + i)
        except:
            print("[本地] 加载技能包失败，忽略：" + i)
            traceback.print_exc()
            pass
    else:
        continue