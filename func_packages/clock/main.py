import schedule as schedule
import model.config
import model.player
import multiprocessing

class Main:

    FUNC_Clock_playPath=""
    music_play_thread=""

    def __init__(self):
        self.path = model.config.APPConfig()
        self.path.setModelName("Clock")
        self.path1 = self.path.getConfig()
        self.FUNC_Clock_playPath=self.path1["playPath"]
        if not self.path1["set_time"] == "0":
            schedule.every().day.at(self.path1["set_time"]).do(self.do_wizz)

    def check(self, string):
        if "闹钟" in string:
            return True
        return False

    def play(self):
        while 1:
            model.player.playsound_from_file(self.FUNC_Clock_playPath,False)

    def do_wizz(self):
        self.music_play_thread = multiprocessing.Process(target=self.play, args=())
        self.music_play_thread.start()

    def main(self,string, boola):
        self.music_play_thread.terminate()
        return {"string": '好的。', "return": 0}