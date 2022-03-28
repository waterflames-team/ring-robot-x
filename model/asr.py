import model.mod_manager

def audioRecorderCallback(fname):  # snowboy to asr
    model.mod_manager.getFunc("ASR")(fname)