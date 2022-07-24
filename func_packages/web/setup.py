import os
import shutil

skill_name="web"
skill_config_name="RingRobotX_Web"

def upgrade():
    os.system("pip3 install tornado asyncio bcrypt websockets nest_asyncio")

def remove():
    os.remove("./config/"+skill_config_name+".json")

def setup():
    os.system("pip3 install tornado asyncio bcrypt websockets nest_asyncio")
    shutil.copy("func_packages/"+skill_name+"/"+skill_config_name+".json", "./config")