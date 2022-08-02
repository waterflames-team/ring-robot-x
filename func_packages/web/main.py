import random
import json
import func_packages.web.server.server
import model.config
import model.logger

def getRandom(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    digits="0123456789"
    ascii_letters="abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_list =[random.choice(digits +ascii_letters) for i in range(randomlength)]
    random_str =''.join(str_list)
    return random_str
  # 版权声明：本文为CSDN博主「日日记」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
  # 原文链接：https://blog.csdn.net/wyy_a/article/details/121632646

if model.config.fastGetConfig("RingRobotX_Web")["first-load"]:
    con=model.config.APPConfig()
    con.setModelName("RingRobotX_Web")
    s=con.getConfig()
    s["password"]=getRandom()
    s["first-load"]=False
    con.setConfig(json.dumps(s))
    model.logger.moduleLoggerMain.info("[RingRobotX_Web] 密码已设置！密码："+s["password"])

func_packages.web.server.server.run()