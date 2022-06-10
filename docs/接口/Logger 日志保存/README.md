例子：

``` python
module_logfile = "./log/main-" + time.strftime("%Y%m%d") + '.log'
moduleLogger = model.logger.AppLogger("RingRobotX-Core-Main", module_logfile)# 注册日志 RingRobotX-Core-Main为名字，module_logfile则是保存路径
moduleLogger.info("logger service started") #输出日志
```