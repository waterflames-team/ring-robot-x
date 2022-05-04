# 查看技能是否合法
import json
import os
import time
import model.logger

import model.config

api_version_CHECK = model.config.fastGetConfig("api-version")

module_logfile = "./log/main-Func-" + time.strftime("%Y%m%d") + '.log'
moduleLogger = model.logger.AppLogger("RingRobotX-Core-Func", module_logfile)


def check_FuncFilePath(path1, file, opt="Func"):
    '''
    检查技能包是否可以导入。
    :param path1: 技能包导入路径
    :param file: 技能包文件夹名
    :param opt: 允许的FuncType（一个！）
    :return: bool
    '''
    try:
        if os.path.exists(os.path.join(path1, file) + '/config.json') == False | os.path.exists(
                os.path.join(path1, file) + '/main.py') == False:
            return False
        with open(os.path.join(path1, file) + '/config.json') as file_obj:  # 打开config
            contents = file_obj.read()
            contents = json.loads(contents)
            if (contents['enable'] == True and contents['funcType'] == opt):  # 技能包启用
                '''
                if contents['apiVersion'] == api_version_CHECK[contents["funcType"]]:
                    return True
                '''
                return True
    except:
        moduleLogger.error('检查技能错误：' + file + "，将忽略")
        traceback.print_exc()
        return False
