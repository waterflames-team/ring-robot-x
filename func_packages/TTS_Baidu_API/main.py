from aip import AipSpeech
import sys
import model.player
import model.hook
import model.config



def main(tts_string):
    # tts
    IS_PY3 = sys.version_info.major == 3
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus

    path = model.config.APPConfig()
    path.setModelName("TTS_BAIDU_API")
    path1 = path.getConfig()

    API_KEY = path1["API_KEY"]
    SECRET_KEY = path1["SECRET_KEY"]

    TEXT = tts_string  # 要识别的文字

    # 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
    # 精品音库：5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美
    PER = path1["PER"]
    # 语速，取值0-15，默认为5中语速
    SPD = path1["SPD"]
    # 音调，取值0-15，默认为5中语调
    PIT = path1["PIT"]
    # 音量，取值0-9，默认为5中音量
    VOL = path1["VOL"]
    # 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
    AUE = 3

    FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
    FORMAT = FORMATS[AUE]

    CUID = path1["APPID"]

    client = AipSpeech(CUID, API_KEY, SECRET_KEY)

    result = client.synthesis(tts_string, 'zh', 1, {
        'spd': SPD,
        'vol': VOL,
        'per': PER,
        'pit':PIT
    })

    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    else:
        raise Exception("音频文件下载失败，请检查网络 "+str(result))

    model.player.playsound_from_file('audio.mp3')

model.hook.add_hook_fast("RRCore.Func.TTS",main)