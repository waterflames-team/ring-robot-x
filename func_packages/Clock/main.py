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
    path = model.config.APPConfig()
    path.setModelName("Clock")
    path1 = path.getConfig()

    FUNC_Clock_playPath=path1["playPath"]
    music_play_thread=""

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

    if not path1["set_time"] == "114514" and not path1["set_time"] == 0:
        schedule.every().day.at(path1["set_time"]).do(do_wizz)