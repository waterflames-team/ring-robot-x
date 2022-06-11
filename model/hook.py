import traceback
import model.logger as logger

HookList = {
    "RRCore.Main.Before.Running":[],
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
    """
    挂上钩子函数到指定的hook
    :param HookName: hook名
    :param HookFunc: hook函数
    :return: 无
    """
    global HookList
    HookList[HookName].append(HookFunc)

def register_hook_fast(HookName):
    """
    初始化hook钩子
    :param HookName: hook钩子名
    :return: 无
    """
    global HookList
    HookList[HookName] = []

def runhook_fast(HookName,*param):
    """
    运行钩子。
    :param HookName: 钩子名
    :param param: 钩子的参数
    :return: 无
    """
    global HookList
    for i in HookList[HookName]:
        try:
            i(*param)
        except:
            logger.moduleLoggerMain.info("[Hook] 报告！Hook " + HookName + " 无法正确加载" + str(i))
            logger.moduleLoggerMain.info(traceback.format_exc())