import model.hook

def audioRecorderCallback(fname):  # snowboy to asr
    model.hook.runhook_fast("RRCore.Model.Before.ASRRunning", fname)
    model.hook.runhook_fast("RRCore.Func.ASR", fname)
    model.hook.runhook_fast("RRCore.Model.After.ASRRunning", fname)