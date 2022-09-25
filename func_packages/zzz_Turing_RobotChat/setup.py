import os
import shutil

skill_name="zzz_Turing_RobotChat"
skill_config_name="Turing_RobotChat"

def upgrade():
    os.system("pip3 install requests")

def remove():
    os.remove("./config/"+skill_config_name+".json")

def setup():
    os.system("pip3 install requests")
    shutil.copy("func_packages/"+skill_name+"/"+skill_config_name+".json", "./config")