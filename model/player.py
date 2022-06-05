import model.logger
import os
import threading
import subprocess

def dele(fpath):
    """
    删除文件
    :param fpath: 文件路径
    :return: 无
    """
    if os.path.exists(fpath):
        os.remove(fpath)

def doPlay(file,dell):
    cmd = ["play", str(file)]
    model.logger.moduleLoggerMain.info("Executing %s", " ".join(cmd))
    proc = subprocess.Popen(
        cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    proc.wait()
    if dell:
        dele(file)
    model.logger.moduleLoggerMain.info("play ok")

def playsound_from_file(file,dell=True):
    """
    播放音频文件
    :param file: 文件路径
    :return: 无
    """
    music_play_thread = threading.Thread(target=doPlay, args=(file,dell))
    music_play_thread.run()  # 开始循环