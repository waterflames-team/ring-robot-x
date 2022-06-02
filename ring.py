# -*- coding: utf-8 -*-

# 这里import model有作用，因为它会使init.py运行，进而初始化所有库文件
# 当然 func_packages也是如此，不过它在func.py导入。
import threading

import schedule
import model
import time

module_logfile = "./log/main-" + time.strftime("%Y%m%d") + '.log'
moduleLogger = model.logger.AppLogger("RingRobotX-Core-Main", module_logfile)
moduleLogger.info("logger service started")

moduleLogger.info(str('''
    RingRobotX
    by LingkongTeam
    {} 加载完毕！
''').format(model.config.fastGetConfig("api-version")["RingRobotX"]))

def worker_cli():
    print("[RingRobotX] CLI模式启动。您现在可以输入")
    while True:
        command=input("[RingRobotX] > ")
        model.hook.runhook_fast("RRCore.Model.FuncAction",command, "print")

def worker_2():
    print("[RingRobotX] Worker schedule running!")
    while True:
        schedule.run_pending()
        time.sleep(1)

worker = threading.Thread(target=worker_2, args=())
worker.start()  # 开始循环
worker1 = threading.Thread(target=worker_cli, args=())
worker1.start()  # 开始循环
# 以下为服务运行区域
time.sleep(2)
model.hook.runhook_fast("RRCore.Main.Before.Running",0)
