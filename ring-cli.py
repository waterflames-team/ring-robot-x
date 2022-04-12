# -*- coding: utf-8 -*-

'''
    RingRobotX - CLIMain
    Author: zhetengtiao(lkteam)
'''
import model
import time

module_logfile = "./log/main-CLI-" + time.strftime("%Y%m%d") + '.log'
moduleLogger = model.logger.AppLogger("RingRobotX-Core-Main-CLI", module_logfile)
moduleLogger.info("logger service started")

moduleLogger.info(str('''
    RingRobotX
    by LingkongTeam
    {} CLI 加载完毕！
''').format(model.config.fastGetConfig("api-version")["RingRobotX"]))

model.hook.runhook_fast("RRCore.Main.Before.Running",0)
model.hook.runhook_fast("RRCore.Main.Before.Running.CLI",0)
while True:
    chat=input()
    model.func.run(chat,"print")