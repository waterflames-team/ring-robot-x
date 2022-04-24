import os
import signal
import sys

import model.asr
import func_packages.Snowboy.snowboydecoder as snowboydecoder
import model.hook
import model.player


interrupted = False

def detectedCallback():
    model.hook.runhook_fast("RRCore.FuncPack.Before.WakeUPRunning",0)
    model.player.playsound_from_file(os.path.split( os.path.realpath( sys.argv[0] ) )[0]+"/"+'assets/music/ding.wav')

def interrupt_callback():
    global interrupted
    return interrupted

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def run():
    modelaa = "assets/snowboy/model.umdl"#自己改唤醒模型路径
    signal.signal(signal.SIGINT, signal_handler)
    detector = snowboydecoder.HotwordDetector(modelaa, sensitivity=0.7)
    detector.start(detected_callback=detectedCallback,
                   audio_recorder_callback=model.asr.audioRecorderCallback,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.01)
    detector.terminate()