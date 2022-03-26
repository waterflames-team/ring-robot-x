# -*- coding: utf-8 -*-

'''
    RingRobotX - CLIMain
    Author: zhetengtiao(lkteam)
'''
import model
import time
import model.func


module_logfile = "./log/main-CLI-" + time.strftime("%Y%m%d") + '.log'
moduleLogger = model.logger.AppLogger("RingRobotX-Core-Main-CLI", module_logfile)
moduleLogger.info("logger service started")

moduleLogger.info('''
    RingRobotX
    Powered by LingkongTeam
    您正在运行命令行对话模式
    Ver.1.0 模块加载中，正在初始化
''')
model.hook.runhook_fast("RRCore.Main.Before.Running",0)
model.hook.runhook_fast("RRCore.Main.Before.Running.CLI",0)
while True:
    chat=input()
    model.func.run(chat,"print")