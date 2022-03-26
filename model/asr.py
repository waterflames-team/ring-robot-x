import base64
import time
import sys
import json
import model.player
import model.func


# asr model from LingkongRobot
def audioRecorderCallback(fname):  # snowboy to asr

    f = open("all.log", 'r')  # 1
    read_log_s = f.read()
    f.close()
    readlog_s = read_log_s

    f = open("fname.txt", 'w+')
    f.write(fname)
    f.close()

    f = open("fname.txt", 'r')
    yuansheng = f.read()

    model.player.playsound_from_file('/assets/music/dong.wav')

    # asr
    IS_PY3 = sys.version_info.major == 3

    if IS_PY3:
        from urllib.request import urlopen
        from urllib.request import Request
        from urllib.error import URLError
        from urllib.parse import urlencode
        timer = time.perf_counter
    else:
        from urllib3 import urlopen
        from urllib3 import Request
        from urllib3 import URLError
        from urllib import urlencode
        if sys.platform == "win32":
            timer = time.clock
        else:

            timer = time.time

    API_KEY = 'kVcnfD9iW2XVZSMaLMrtLYIz'
    SECRET_KEY = 'O9o1O213UgG5LFn0bDGNtoRN3VWl2du6'

    def asr(file):
        global AUDIO_FILE, result_str
        global FORMAT
        AUDIO_FILE = file
        FORMAT = AUDIO_FILE[-3:]

    # 文件后缀只支持pcm/wav/amr格式

    asr(fname)  # 需要识别的文件

    CUID = '123456PYTHON'
    # 采样率
    RATE = 16000  # 固定值

    # 普通版

    DEV_PID = 1536  # 1537 表示识别普通话，使用输入法模型。1536表示识别普通话，使用搜索模型。根据文档填写PID，选择语言及识别模型
    ASR_URL = 'http://vop.baidu.com/server_api'
    SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有

    class DemoError(Exception):
        pass

    """  TOKEN start """

    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'

    def fetch_token():

        params = {'grant_type': 'client_credentials',
                  'client_id': API_KEY,
                  'client_secret': SECRET_KEY}
        post_data = urlencode(params)
        if (IS_PY3):
            post_data = post_data.encode('utf-8')
        req = Request(TOKEN_URL, post_data)
        try:
            f = urlopen(req)
            result_str = f.read()
        except URLError as err:
            # print('token http response http code : ' + str(err.code))
            result_str = err.read()
        if (IS_PY3):
            result_str = result_str.decode()

        # print(result_str)
        result = json.loads(result_str)
        # print(result)
        if ('access_token' in result.keys() and 'scope' in result.keys()):
            # print(SCOPE)
            if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
                raise DemoError('scope is not correct')
            # print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
            return result['access_token']
        else:
            raise DemoError(
                'MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

    """  TOKEN end """

    if __name__ == '__main__':
        token = fetch_token()

        speech_data = []
        global AUDIO_FILE
        with open(AUDIO_FILE, 'rb') as speech_file:
            speech_data = speech_file.read()

        length = len(speech_data)
        if length == 0:
            raise DemoError('file %s length read 0 bytes' % AUDIO_FILE)
        speech = base64.b64encode(speech_data)
        if (IS_PY3):
            speech = str(speech, 'utf-8')
        global FORMAT
        params = {'dev_pid': DEV_PID,
                  # "lm_id" : LM_ID,    #测试自训练平台开启此项
                  'format': FORMAT,
                  'rate': RATE,
                  'token': token,
                  'cuid': CUID,
                  'channel': 1,
                  'speech': speech,
                  'len': length
                  }
        post_data = json.dumps(params, sort_keys=False)

        req = Request(ASR_URL, post_data.encode('utf-8'))
        req.add_header('Content-Type', 'application/json')
        try:
            begin = timer()
            f = urlopen(req)
            result_str = f.read()
            # print ("Request time cost %f" % (timer() - begin))
        except URLError as err:
            # print('asr http response http code : ' + str(err.code))
            result_str = err.read()

        if (IS_PY3):
            # global cg
            # cg = result_str['result'][0]
            # cg = result_str.json['result']
            result_str = str(result_str, 'utf-8')
        # print(result_str)
        with open("result.txt", "w") as of:
            of.write(result_str)

    '''
    cg = result_str

    cg = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", cg)
    cg = re.sub(r'}', '', cg)
    cg = re.sub(r'{', '', cg)
    cg = re.sub(r'_', '', cg)
    cg = re.sub(r'"', '', cg)
    cg = re.sub(r':', '', cg)
    log_log.logger.debug('成功识别到文字')
    log_log.logger.debug(cg)
    #令人震惊的去杂符号操作


    '''
    cg = json.loads(result_str)

    cg = cg['result'][0]

    model.func.run(cg)  # 调用技能

    # asr

    f = open("all.log", 'r')  # 2
    read_log_s = f.read()
    f.close()
    readlog_s = read_log_s
