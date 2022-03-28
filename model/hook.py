from datetime import time

import model

HookList = {
    "RRCore.Main.Before.Running":[],
    "RRCore.Main.Before.Running.CLI":[],
    "RRCore.Model.Before.FuncRunning":[],
    "RRCore.Model.After.FuncRunning":[]
}

def add_hook_fast(HookName,HookFunc):
    global HookList
    HookList[HookName].append(HookFunc)

def register_hook_fast(HookName):
    global HookList
    HookList[HookName] = []

def runhook_fast(HookName,returnValue):
    global HookList
    for i in HookList[HookName]:
        i(returnValue)