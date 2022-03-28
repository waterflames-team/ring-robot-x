import os
import signal
import sys

import model.asr
import model.snowboydecoder as snowboydecoder


interrupted = False

def detectedCallback():
    model.player.playsound_from_file(os.path.split( os.path.realpath( sys.argv[0] ) )[0]+"/"+'assets/music/ding.wav')

def interrupt_callback():
    global interrupted
    return interrupted

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

# TODO 这里的todo是为了引起你的注意。
# 如果你需要使用自定义唤醒引擎，那么你可以直接将config.json的enable变为false，然后下载其他引擎，导入到func_packages
# 这样了话，系统不会导入snowboy库，而是你的自定义会代替snowboy运行。

modelaa = "assets/snowboy/model.pmdl"#自己改唤醒模型路径
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(modelaa, sensitivity=0.7)
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=model.asr.audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)
detector.terminate()
print("Snowboy ready!")