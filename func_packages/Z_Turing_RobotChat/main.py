import json
import model.config
import requests


class Main:
    def check(self, string):
        # 检查字符串是否可以归于该扩展管辖
        return True

    def main(self, string, bool):
        path = model.config.APPConfig()
        path.setModelName("ASR_BAIDU_API")
        path1 = path.getConfig()

        url = 'http://openapi.tuling123.com/openapi/api/v2'
        city = path1["city"]

        apikey = path1["apikey"]
        userid = path1["userId"]

        '''
        较多人使用同样5个apikey，一天只能调用500次，难免会不够，
        所以有能力的小伙伴我推荐自己去图灵机器人的首页注册一个自己的账号，实名制一下
        然后把机器人管理页面的右上角的账号填到"userId"的冒号后面（在下面的req>"userInfo">"userId"里）
        我这里的apikey只给实在是没能力去实名制使用的人以及灵空机器人的测试员
        '''

        a = string
        req = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": a
                },
                "inputImage": {
                    "url": "imageUrl"
                },
                "selfInfo": {
                    "location": {
                        "city": city,
                    }
                }
            },
            "userInfo": {
                "apiKey": apikey,
                "userId": userid
            }
        }
        req = json.dumps(req).encode('utf8')
        post = requests.post(url, data=req, headers={'content-type': 'application/json'})
        r = post.text
        r = r.encode('utf8')
        r = json.loads(r)
        text = r['results'][0]['values']['text']

        return {"string": text, "return": 0}
