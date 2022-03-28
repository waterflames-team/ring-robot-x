import func_packages

functions = {
    "TTS": [],
    "ASR": []
}


def setFunc(func, name):
    global functions
    if functions[name] is None:
        functions[name] = []
    functions[name].append(func)
    print("[本地] 技能扩展包新增：" + name)


def getFunc(name):
    global functions
    if not functions[name]:
        functions[name] = [print]
    return functions[name][0]
