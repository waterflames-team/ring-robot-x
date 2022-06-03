# -*- coding: utf-8 -*-
import logging
import time

class AppLogger:
    def __init__(self, moduleName, logfile):
        """
        初始化
        :param moduleName: 模块名
        :param logfile: log的文件名
        """
        self._logger = logging.getLogger(moduleName)

        self._logger.handlers.clear() #清除已有logger，避免重复记录

        handler = logging.FileHandler(logfile,encoding='utf-8')

        fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(message)s"
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        self._logger.addHandler(console)
        self._logger.setLevel(logging.INFO)

        self.warnning = self._logger.warning
        self.error = self._logger.error
        self.info = self._logger.info
        self.debug = self._logger.debug


# del moduleLogger

module_logfileMain = "./log/" + time.strftime("%Y%m%d") + '.log'
moduleLoggerMain = AppLogger("RingRobotX-Core-Main", module_logfileMain)
moduleLoggerMain.info("logger service started")
