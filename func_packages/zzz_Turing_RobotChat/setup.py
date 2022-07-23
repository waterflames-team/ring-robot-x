import os


def upgrade():
    os.system("pip3 install requests")

def remove():
    os.remove("./config/Turing_RobotChat.json")

def setup():
    os.system("pip3 install requests")
    os.system('cp -f ./func_packages/zzz_Turing_RobotChat/Turing_RobotChat.json ./config')