import model.mod_manager


def tts(tts_string):
    model.mod_manager.getFunc("TTS")(tts_string)
