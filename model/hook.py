from datetime import time

import model

HookList = {
    "RRCore.Main.Before.Running":[],
    "RRCore.Main.Before.Running.CLI":[],
    "RRCore.Model.Before.FuncRunning":[],
    "RRCore.Model.After.FuncRunning":[]
}

def register_hook_fast(HookName):
    HookList[HookName] = []

def runhook_fast(HookName,returnValue):
    for i in HookList[HookName]:
        i(returnValue)

class HookerRegister(object):

    HookName=None

    def __init__(self,HookName):
        self.HookName=HookName
        HookList[HookName]=[]

    def run_Hook(self,returnValue,HookName=None):
        if HookName==None:
            HookName=self.HookName
        for i in HookList[HookName]:
            i(returnValue)

class HookClient(object):
    def hookEverything(self,HookName,Function):
        HookList[HookName].append(Function)
        return True