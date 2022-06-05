import importlib
import os
import signal
import sys

import model.asr
import model.hook
import model.player


interrupted = False

def detectedCallback():
    if model.config.fastGetConfig("func")["dontshout"]:
        return
    model.hook.runhook_fast("RRCore.FuncPack.Before.WakeUPRunning",0)
    model.player.playsound_from_file(os.path.split( os.path.realpath( sys.argv[0] ) )[0]+"/"+'assets/music/ding.wav',False)

def interrupt_callback():
    global interrupted
    return interrupted

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def run(i):
    a=importlib.import_module("func_packages.Snowboy.snowboydecoder")
    modelaa = "config/snowboy/model.pmdl"#自己改唤醒模型路径
    signal.signal(signal.SIGINT, signal_handler)
    detector = a.HotwordDetector(modelaa, sensitivity=0.7)
    detector.start(detected_callback=detectedCallback,
                   audio_recorder_callback=model.asr.audioRecorderCallback,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.01)
    detector.terminate()