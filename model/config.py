import os
import json

def fastGetConfig(modelName,fileType="json",encode='utf-8'):
    """
    一个函数解决get config
    :param modelName: 模块名（config文件名
    :param fileType: 文件后缀（可选）
    :param encode: 解码方式（可选）
    :return: json对象或字符串
    """
    with open('./config/' + modelName + '.' + fileType, encoding=encode) as file_obj:
        contents = file_obj.read()
        if fileType == "json":
            return json.loads(contents)
        else:
            return contents

class APPConfig(object):

    modelName=""
    def __init__(self):
        self.modelName=""

    def setModelName(self,name):
        """
        设置模块名
        :param name: 模块名
        :return: 无
        """
        self.modelName=name

    def getConfig(self,fileType="json",encode='utf-8'):
        """
        获取config
        :param fileType: 文件后缀（可选）
        :param encode: 解码方式（可选）
        :return: json对象或字符串
        """
        with open('./config/'+self.modelName+'.'+fileType, encoding=encode) as file_obj:
            contents = file_obj.read()
            if fileType== "json":
                return json.loads(contents)
            else:
                return contents

    def setConfig(self,stringContent,fileType='json',encode='utf-8'):
        """
        设置config
        :param stringContent: 欲写入的字符串
        :param fileType: 文件后缀（可选）
        :param encode: 解码方式（可选）
        :return: 无
        """
        with open('./config/'+self.modelName+'.'+fileType,"w", encoding=encode) as file:
            file.write(stringContent)