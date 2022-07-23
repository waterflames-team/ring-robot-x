import os


def upgrade():
    return

def remove():
    os.remove("./config/Clock.json")
    return

def setup():
    os.system('cp -f ./func_packages/Clock/Clock.json /config')
    return