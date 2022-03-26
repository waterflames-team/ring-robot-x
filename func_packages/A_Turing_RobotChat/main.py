import json
import random
import requests

def check(string):
    #检查字符串是否可以归于该扩展管辖
    return True

def main(string, bool):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    city = "福州"  # 请自行在这里修改城市为自己的城市

    sj = random.randint(1, 5)
    if sj == 1:
        apikey = "197deae9fb5c4fb3bfd970d82917aeb0"
        pass
    if sj == 2:
        apikey = "ed984644aa50485ea0106b941de1f521"
        pass
    if sj == 3:
        apikey = "22fdeb0cfcc146b0a3acb76241d80eaf"
        pass
    if sj == 4:
        apikey = "e9c5c5121ccd4450a559c77fdc934b8a"
        pass
    if sj == 5:
        apikey = "3a952ac21d8a4c079e59aedc36791bb2"
        pass

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
            "userId": "450562"  # 如果你改了apikey，请把这也改了
        }
    }
    req = json.dumps(req).encode('utf8')
    post = requests.post(url, data=req, headers={'content-type': 'application/json'})
    r = post.text
    r = r.encode('utf8')
    r = json.loads(r)
    text = r['results'][0]['values']['text']

    return {"string": text, "return": 0}
