from playsound import playsound # 导包
import os

def dele(fpath):
    """
    删除文件
    :param fpath: 文件路径
    :return: 无
    """
    if os.path.exists(fpath):
        os.remove(fpath)

def playsound_from_file(file):
    """
    播放音频文件
    :param file: 文件路径
    :return: 无
    """
    playsound(file)