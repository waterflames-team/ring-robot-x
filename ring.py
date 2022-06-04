# -*- coding: utf-8 -*-
import argparse
import importlib
import traceback

parser = argparse.ArgumentParser(description='RingRobotX - By LingkongTeam')
parser.add_argument('--no-cli', dest='cli', help='不需要CLI模式 | No CLI',action="store_true",default=False)
args = parser.parse_args()

# 这里import model有作用，因为它会使init.py运行，进而初始化所有库文件
# 当然 func_packages也是如此，不过它在func.py导入。

import threading
import schedule
import model
import time

model.logger.moduleLoggerMain.info(str('''
    RingRobotX
    by LingkongTeam
    {} 加载完毕！
''').format(model.config.fastGetConfig("api-version")["RingRobotX"]))

#============================ 重加载指令注册 ============================

def reload_com(string):
    if string=="func":
        model.func.reload()
    elif string=="model":
        importlib.reload(model)
    elif string=="all":
        model.func.reload()
        importlib.reload(model)
    else:
        return "string is missing"
    return "success"

model.cli.command_registry("reload",reload_com)
model.cli.help_registry("reload","reload [model/func/all] | 重新加载模块")

def exit_com():
    exit(0)

model.cli.command_registry("exit",exit_com)
model.cli.help_registry("exit","exit | 停止运行RingRobotX")

#============================ 重加载指令注册 ============================

def worker_cli():
    cli=model.cli.console()
    print("[RingRobotX] CLI模式启动。您现在可以输入")
    while True:
        command=input("[RingRobotX] > ")
        clist=command.split()
        try:
            command=clist[0]
            clist.pop(0)
        except:
            model.logger.moduleLoggerMain.info("[CLI] 报告！您的命令无法解析。")
            model.logger.moduleLoggerMain.info(traceback.format_exc())
            continue
        cli.commandRun(command,tuple(clist))

def worker_2():
    model.logger.moduleLoggerMain.info("[RingRobotX] Worker schedule running!")
    while True:
        schedule.run_pending()
        time.sleep(1)

worker = threading.Thread(target=worker_2, args=())
worker.start()  # 开始循环

if __name__ == "__main__":
    if not args.cli:
        worker1 = threading.Thread(target=worker_cli, args=())
        worker1.start()  # 开始循环
    # 以下为服务运行区域
    time.sleep(2)
    model.hook.runhook_fast("RRCore.Main.Before.Running", 0)
else:
    model.logger.moduleLoggerMain.info("[RingRobotX] 检测到模块形式导入，将不启动cli和beforeRunning Hook。请注意：这种启动方式会让其它脚本控制RingRobotX，请确认你启动的程序是你信任的程序。")