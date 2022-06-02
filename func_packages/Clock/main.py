import threading
import inspect
import ctypes

import schedule as schedule


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

from playsound import playsound # 导包
import model.config

class Main:

    FUNC_Clock_playPath=""
    music_play_thread=""

    def __init__(self):
        self.path = model.config.APPConfig()
        self.path.setModelName("Clock")
        self.path1 = self.path.getConfig()
        self.FUNC_Clock_playPath=self.path1["playPath"]
        if not self.path1["set_time"] == "114514" and not self.path1["set_time"] == 0:
            schedule.every().day.at(self.path1["set_time"]).do(self.do_wizz)

    def check(self, string):
        if "闹钟" in string:
            return True
        return False

    def play(self):
        while 1:
            playsound(self.FUNC_Clock_playPath)

    def do_wizz(self):
        self.music_play_thread = threading.Thread(target=self.play, args=())
        self.music_play_thread.run()  # 开始循环

    def main(self,string, boola):
        stop_thread(self.music_play_thread)
        return {"string": '好的。', "return": 0}