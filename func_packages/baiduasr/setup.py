import os
import platform
import shutil

skill_name="baiduasr"
skill_config_name="ASRBaidu"

def upgrade():
    os.system("pip3 install baidu-aip")

def remove():
    os.remove("./config/"+skill_config_name+".json")

def setup():
    os.system("pip3 install baidu-aip")
    shutil.copy("func_packages/"+skill_name+"/"+skill_config_name+".json", "./config")