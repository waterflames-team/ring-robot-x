import os


def upgrade():
    os.system("pip3 install tornado asyncio bcrypt websockets nest_asyncio")

def remove():
    os.remove("./config/RingRobotX_Web.json")

def setup():
    os.system("pip3 install tornado asyncio bcrypt websockets nest_asyncio")
    os.system('cp -f ./func_packages/RingRobotX_Web/RingRobotX_Web.json ./config')