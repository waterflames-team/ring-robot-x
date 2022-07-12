import random
import cn2an


class Main:
    FUNC_GuessNumber_Number = 0

    def check(self, string):
        if "猜数字" in string:
            return True
        return False

    def main(self,string, boola):

        if not boola:
            self.FUNC_GuessNumber_Number = random.randint(1, 100)
            #print(self.FUNC_GuessNumber_Number)
            return {"string": "你好~来玩猜数字吧~请猜一个1到100之间的秘密数字", "return": 1}

        if "不玩了" in string or "退出" in string:
            return {"string": '好吧...', "return": 0}

        #print(self.FUNC_GuessNumber_Number)

        string = int(cn2an.cn2an(string,"smart"))

        if string == self.FUNC_GuessNumber_Number:
            return {"string": str(string) + '就是秘密数字！恭喜你猜对了！', "return": 0}

        if string > self.FUNC_GuessNumber_Number:
            return {"string": '猜大了，请再来一次！', "return": 1}
        if string < self.FUNC_GuessNumber_Number:
            return {"string": '猜小了，请再来一次！', "return": 1}
