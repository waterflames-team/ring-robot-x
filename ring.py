# -*- coding: utf-8 -*-
'''
    RingRobotX - Main
    Author: zhetengtiao(lkteam)
'''
# 这里import model有作用，因为它会使init.py运行，进而初始化所有库文件
# 当然 func_packages也是如此，不过它在func.py导入。
import model
import time
import model.player

module_logfile = "./log/main-" + time.strftime("%Y%m%d") + '.log'
moduleLogger = model.logger.AppLogger("RingRobotX-Core-Main", module_logfile)
moduleLogger.info("logger service started")

moduleLogger.info('''
    RingRobotX
    by LingkongTeam
    Ver.1.0 模块加载中，正在初始化
''')

# 以下为服务运行区域

model.hook.runhook_fast("RRCore.Main.Before.Running",0)

# Sleep forever
from time import sleep
while True:
    sleep(10)