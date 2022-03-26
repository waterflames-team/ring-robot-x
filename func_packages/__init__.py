# -*- coding: utf-8 -*-
import importlib
import os
import pkgutil

#模块化自动引入

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

for i in os.listdir(r''+path):
    if os.path.isdir(path+"/"+i) and i!="__pycache__":
        try:
            importlib.import_module(name + '.' + i)
            print("[本地] 成功加载技能包：" + i)
        except:
            print("[本地] 加载技能包失败，忽略：" + i)
            pass
    else:
        continue