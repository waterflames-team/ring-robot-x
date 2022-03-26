import os
import json

class APPConfig(object):

    modelName=""
    def __init__(self):
        self.modelName=""

    def setModelName(self,name):
        self.modelName=name

    def getConfig(self,fileType="json",encode='utf-8'):
        with open('./config/'+self.modelName+'.'+fileType, encoding=encode) as file_obj:
            contents = file_obj.read()
            if(fileType=="json"):
                return json.loads(contents)
            else:
                return contents

    def setConfig(self,stringContent,fileType='json',encode='utf-8'):
        with open('./config/'+self.modelName+'.'+fileType,"w", encoding=encode) as file:
            file.write(stringContent)