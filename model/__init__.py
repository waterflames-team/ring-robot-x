# -*- coding: utf-8 -*-
import importlib
import os
import pkgutil
import traceback

# 模块化自动引入

print("[本地] 正在加载模块")

path = os.path.dirname(__file__)
name = os.path.basename(path)

for _, file, _ in pkgutil.iter_modules([path]):
    try:
        importlib.import_module(name + '.' + file)
    except:
        print("[本地] 加载模块失败，忽略：" + file)
        traceback.print_exc()
        pass
