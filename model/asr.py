import model.hook


def audioRecorderCallback(fname):
    """
    asr运行。
    :param fname: file name 录音文件名
    :return: 无
    """
    if model.config.fastGetConfig("func")["dontshout"]:
        return
    model.hook.runhook_fast("RRCore.Model.Before.ASRRunning", fname)
    model.hook.runhook_fast("RRCore.Func.ASR", fname)
    model.hook.runhook_fast("RRCore.Model.After.ASRRunning", fname)
