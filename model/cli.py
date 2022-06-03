import traceback
import model.hook
import model.logger as logger
import requests
import model.config
import json

def hook_com(runMode,hookName):
    if runMode=="reg":
        model.hook.register_hook_fast(hookName)
        return "success"
    elif runMode=="run":
        model.hook.runhook_fast(hookName)
        return "success"
    else:
        return "runMode is missing"

def func_com(string,tts="tts"):
    model.func.run(string,tts)
    return "success"

def tts_com(string):
    model.tts.tts(string)
    return "success"

def asr_com(string):
    model.asr.asr(string)
    return "success"

def help_com(y):
    print("已加载命令：")
    for key, value in commands.items():
        print(key,end=" ")
    print()
    print("hook [runmode] [hookname] | runmode可输入reg或run，分别代表初始化hook列表和运行hook")
    print("func [string] | 输入你想对RingRobotX说的话。")
    print("tts [string] | 运行tts ===== asr [path] | 运行asr")
    print("reload [model/func/all] | 重新加载模块")
    print("check-update | 检查更新")
    print("update | 更新程序")
    print("其他模块详细使用方法请参见模块文档")
    return "success"

def hello_ringrobotx():
    print("Now playing: Rick Astley - Never Gonna Give You Up")
    return "Hello RingRobotX"

def check_update():
    now=model.config.fastGetConfig("api-version")
    response = requests.get('https://gitee.com/lkteam/ring-robot-x/raw/'+now["branch"]+'/config/api-version.json')
    if float(json.loads(response.text)["RingRobotX"]) > float(now["RingRobotX"]):
        return "Yes"
    else:
        return "No"

def update_robotx(yesorno='mita'):
    if yesorno == "mita":
        logger.moduleLoggerMain.info("[CLI] 更新前，程序会将config目录备份。更新后，除了config目录，您对于程序源代码所做出的改动会被覆盖！开发人员不为您数据的损失负责！确认继续请输入 update y")
        return "[CLI] 更新前，程序会将config目录备份。更新后，除了config目录，您对于程序源代码所做出的改动会被覆盖！开发人员不为您数据的损失负责！确认继续请输入 update y"
    else:
        os.system('cp ./config/ ../config && git fetch --all && git reset --hard origin/'+model.config.fastGetConfig("api-version")["branch"]+' && git pull && mv -f ../config/ ./config')# 摆烂型更新
        return "success"
    # cp ./config/ ../config && git pull && mv ../config/ /config

commands={
    "hook":hook_com,
    "func":func_com,
    "tts":tts_com,
    "asr":asr_com,
    "help":help_com,
    "hello":hello_ringrobotx,
    "check-update":check_update,
    "update":update_robotx
}

def command_registry(command,func):
    global commands
    commands[command]=func

class console(object):
    def commandRun(self,command,param):
        try:
            logger.moduleLoggerMain.info("[CLI] 运行指令：" + command + " 参数"+str(*param))
            ret=commands[command](*param)
            logger.moduleLoggerMain.info("[CLI] 指令返回：" + ret)
        except:
            logger.moduleLoggerMain.info("[CLI] 报告！指令" + command + " 无法正确加载")
            logger.moduleLoggerMain.info(traceback.format_exc())