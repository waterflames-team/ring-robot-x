import os
import shutil

skill_name="clock"
skill_config_name="clock"

def upgrade():
    return

def remove():
    os.remove("./config/"+skill_config_name+".json")

def setup():
    shutil.copy("func_packages/"+skill_name+"/"+skill_config_name+".json", "./config")