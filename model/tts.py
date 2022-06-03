import model.hook


def tts(tts_string):
    """
    运行tts
    :param tts_string: tts的字符串
    :return: 无
    """
    model.hook.runhook_fast("RRCore.Model.Before.TTSRunning", tts_string)
    model.hook.runhook_fast("RRCore.Func.TTS", tts_string)
    model.hook.runhook_fast("RRCore.Model.Before.TTSRunning", tts_string)
