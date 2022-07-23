import os


def upgrade():
    os.system("pip3 install baidu-aip")

def remove():
    os.remove("./config/TTS_BAIDU_API.json")

def setup():
    os.system("pip3 install baidu-aip")
    os.system('cp -f ./func_packages/TTS_BAIDU_API/TTS_BAIDU_API.json ./config')