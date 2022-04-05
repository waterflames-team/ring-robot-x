import model.hook


def tts(tts_string):
    model.hook.runhook_fast("RRCore.Model.Before.TTSRunning", tts_string)
    model.hook.runhook_fast("RRCore.Func.TTS", tts_string)
    model.hook.runhook_fast("RRCore.Model.Before.TTSRunning", tts_string)
