import os


def upgrade():
    print("upgraded.")
    os.system("pip3 install baidu-aip")

def remove():
    os.remove("./config/ASR_BAIDU_API.json")

def setup():
    os.system("pip3 install baidu-aip")
    os.system('cp -f ./func_packages/ASR_BaiduASR_API/ASR_BAIDU_API.json /config')