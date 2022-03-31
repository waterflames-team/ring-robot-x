import model.mod_manager
import model.hook

def audioRecorderCallback(fname):  # snowboy to asr
    model.hook.runhook_fast("RRCore.Model.Before.ASRRunning", fname)
    model.mod_manager.getFunc("ASR")(fname)
    model.hook.runhook_fast("RRCore.Model.After.ASRRunning", fname)