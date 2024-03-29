# 普通技能包

**请在观看本页面前先了解“入前须知”**

创建一个技能包十分简单，以本教程为例，我们在 func_packages 目录中创建一个文件夹，取名为 A_HelloRing

其次，我们还需要创建一些文件，像这样：

```
RingRobotX
├─func_packages
│  ├─A_HelloRing
|     ├─config.json
|     ├─main.py
|     ├─setup.py
```

## config.json
config.json示例:

```json
{
  "name": "A_HelloRing",
  "enable": true,
  "funcType": "Func",
  "version": 1,
  "apiVersion": "Beta.3",
  "RingRobotX-Ver": 2.6,
  "Author": "Myself",
  "need_first_load": true,
  "description": "test."
}
```
* name的值为文件夹的名字，文件夹的名字就是技能的名字
* enable是否为true决定着插件是否启用
* funcType值可以为Func，ASR，TTS，WakeUP，Otherwise
* version是你的技能的版本（float类型）
* RingRobotX-Ver是你的技能最低支持RingRobotX的什么版本
* need_first_load 表示此技能包是否需要初始化（见下文
* Author为作者，description为备注

**一般情况下，RingRobotX的插件系统是向下兼容的，当然也有的插件可能出现不兼容新版的情况**

## setup.py

另外，如果要将此插件分发给他人，你还需要初始化

rrx根据config.json中的need_first_load 判断是否需要初始化，当need_first_load为true时，它将会尝试初始化，如下表：

* 当需要初始化时，运行技能目录中的setup.py中的setup函数
* 当marx（rrx的技能包管理器）收到此技能需要更新时：在替换较新版本技能代码后，运行技能目录中的setup.py中的upgrade函数。
* 当marx收到此技能需要移除时，运行技能目录中的setup.py中的remove函数，并在运行完毕之后自动删除技能目录。

所以，你的setup.py至少应该这样：（以guessnumber技能为例）
```python
import os


def upgrade():
    os.system("pip3 install cn2an") #更新时安装cn2an包

def remove():
    return 

def setup():
    os.system("pip3 install cn2an") #安装时安装cn2an包
```

## main.py

main.py示例:

```python
class Main:    
    def check(string):
        if "灵空" in string: #检测到词语
            return True #返回True后rrx会运行此class中的main函数
        return False
    def main(string,bool):#string为传入的整句话，bool则为连续对话是否开启
        if "取消连续对话" in string:
            return {"string":"好的","return":0}# return为0即关闭连续对话
        if "开启连续对话" in string:
            return {"string":"好的","return":1}# return为1即开启连续对话
        else:
            return {"string":"哎呀，我听不懂呢~","return":0}
```

main.py需要有一个class：Main和最基本的两个函数：check和main

check有一个参数：string（用户说给ringrobot的话），你可以在check函数里鉴定这句话是不是需要你回答

如果需要这个技能回答，就返回 True ，否返回 False

比如，询问天气：
```python
def check(string):
    if "天气" in string:
        return True
    return False
```

如果我们说了包含“天气”的话，那么这个技能包就会为你服务。

(注：如果你觉得这种不够【智能】，那么你可以使用语义理解等方式判断，一切在于你，而不是ringrobot)

那么怎么让技能包为我们服务呢？

main函数包括两个参数：string（用户说给ringrobot的话）和bool（是否在连续对话模式）。

然后你的技能包在处理完之后，将返回的句子+是否启用连续对话打包为字典return回去

比如，我们要传回text为我们的答复：

```python
return {"string": text, "return": 0} # 0（False）代表不启用，1（True）代表启用
```

setup.py需要定义三个函数：upgrade、remove、setup

当技能发生更新、删除、安装时，mariner会调用这三个函数

你可以使用这个特性，来完成“技能安装时安装依赖”的操作

至此，技能包开发完成，和你的小伙伴一起分享吧！

示例：见仓库func_packages文件夹自带技能包