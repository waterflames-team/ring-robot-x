import model.mod_manager
import model.hook


def tts(tts_string):
    model.hook.runhook_fast("RRCore.Model.Before.TTSRunning", tts_string)
    model.mod_manager.getFunc("TTS")(tts_string)
    model.hook.runhook_fast("RRCore.Model.Before.TTSRunning", tts_string)
