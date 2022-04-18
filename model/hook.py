import traceback

HookList = {
    "RRCore.Main.Before.Running":[],
    "RRCore.Main.Before.Running.CLI":[],
    "RRCore.Model.Before.FuncRunning":[],
    "RRCore.Model.After.FuncRunning":[],
    "RRCore.Model.After.ContinueDisable":[],
    "RRCore.Model.After.ContinueEnable":[],
    "RRCore.Model.Before.TTSRunning":[],
    "RRCore.Model.After.TTSRunning":[],
    "RRCore.Model.Before.ASRRunning":[],
    "RRCore.Model.After.ASRRunning":[],
    "RRCore.FuncPack.Before.WakeUPRunning":[],
    "RRCore.Func.TTS":[],
    "RRCore.Func.ASR":[],
    "RRCore.Model.FuncAction":[]
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
        try:
            i(returnValue)
        except:
            print("【hook】报告！hook"+HookName+" 无法正确加载"+str(i))
            traceback.print_exc()