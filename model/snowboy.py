import signal
import model.asr
import model.snowboydecoder as snowboydecoder


interrupted = False

def detectedCallback():
    model.player.play('assets/music/ding.wav')

def interrupt_callback():
    global interrupted
    return interrupted

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

# TODO 这里的todo是为了引起你的注意。
# 如果你需要使用自定义唤醒引擎，那么你可以直接将下面内容注释掉，并且新建一个py文件，将初始化直接放到py最外面，使系统导入你的py时运行即可。
# 这样了话，系统虽然也会导入snowboy库，但是snowboy库不会自动运行，而是你的自定义会代替snowboy运行。
# 自定义asr修改audio_recorder_callback

modelaa = "assets/snowboy/model.umdl"#自己改唤醒模型路径
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(modelaa, sensitivity=0.7)
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=model.asr.audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)
detector.terminate()
