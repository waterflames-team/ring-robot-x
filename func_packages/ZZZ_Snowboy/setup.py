import os


def upgrade():
    return

def remove():
    os.remove("./snowboy/*")
    return

def setup():
    os.system('''
    git clone https://gitee.com/zhetengtiao/snowboy.git &&
    cd snowboy/swig/Python3 &&
    make &&
    cp snowboy/swig/Python3/_snowboydetect.so ring-robot-x/func_packages/ZZZ_Snowboy &&
    cp snowboy/examples/Python3/snowboydetect.py ring-robot-x/func_packages/ZZZ_Snowboy &&
    cp -a snowboy/resources/ ring-robot-x/func_packages/ZZZ_Snowboy/resources &&
    ''')