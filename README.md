# RingRobotX - 灵活易开发的语音对话机器人框架

这是一个python语音对话机器人框架，根据LingkongRobot修改而来
特色功能：

1. 模块化管理（技能扩展包，功能扩展包）
2. 我们都喜欢的命令行！你可以通过命令行直接对话
3. 配置简单化，配置可以在config目录修改，避免直接修改源代码
4. 实现了连续对话 - 终于可以和机器人玩成语接龙了
5. 从根部开始重构 - 摆脱LingkongRobot旧版本的600行文件
6. 开放，简洁的接口，您可以迅速入手框架并自定义自己的使用方式
7. 没有复杂死板的封装，所有功能都使用巧妙的注册函数调用
8. 因为架构的灵活性，tts、asr、唤醒等等功能都具有高度的模块化，高度可自定义

好了，准备好体验激动人心的RingRobot了吗？现在开始！

# 须知

RingRobotX 是lingkongteam成员“zhetengtiao”自行重构，（可能）并不在lingkongrobot 重构计划范围内。

请期待lingkongrobot 重构版！

RingRobotX默认（git仓库版本）内置图灵、百度ASR&TTS、snowboy唤醒插件

即使你不会python，申请了图灵、百度apikey后仍然可以玩转它

后期将会着重开发插件，注重功能的扩展加强

（是的即使snowboy死了但是还能耍

在线模型训练：https://snowboy.hahack.com/

感谢wzpan老师的搭建）

# 安装

## 方案1：自动安装脚本

自动安装脚本只支持使用apt的linux发行版。

运行：
```shell
wget -O install.sh https://gitee.com/lkteam/ring-robot-x/raw/master/install.sh && sudo bash install.sh
```

当然，如果你是其他发行版，可以试着第二种方案：手动安装。

## 方案2：手动安装

### 1.安装RingRobotX

```shell
sudo apt install python3 python3-pip git python3-pyaudio swig libatlas-base-dev pulseaudio make alsa-utils
pip3 install pydub playsound
git clone https://gitee.com/lkteam/ring-robot-x
```

运行此命令后，ring将会下载到命令执行的目录

当然，如果你追求稳定，可以从我们的项目主页下载发行版

如果你追求新功能，请下载develop版本

### 2.安装语音唤醒功能

唤醒功能依赖[snowboy](https://github.com/Kitt-AI/snowboy.git)

为了避免某些问题，snowboy暂时不会集成到ringrobotx

所以，我们需要手动安装snowboy

请执行以下命令：

```shell
git clone https://github.com/Kitt-AI/snowboy.git
cd snowboy/swig/Python3
make
cd ../../../
cp snowboy/swig/Python3/_snowboydetect.so ring-robot-x/model
cp snowboy/examples/Python3/snowboydecoder.py ring-robot-x/model
cp snowboy/examples/Python3/snowboydetect.py ring-robot-x/model
cp -a snowboy/resources/ ring-robot-x/model/resources
```

# 运行

```shell
python3 ring.py
```

哦对了，内置的模型唤醒词是“灵空灵空”

你可以替换掉，它在assets/snowboy/model.umdl

# 设置

详见config目录下的各种json文件

# 框架接口
## 技能包创建

创建一个技能包十分简单，你只需要在func_packages新建一个文件夹，名字随意

新建一个main.py和config.json，config.json需要包含"enable":true,和"funcType":"Func"这样系统才会认为技能包可使用

随后，main.py需要有最基本的两个函数：check和main

check有一个参数：string（用户说给ringrobot的话），你可以在check函数里鉴定这句话是不是需要你回答

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

至此，技能包开发完成，和你的小伙伴一起分享吧！

示例：见仓库func_packages文件夹自带技能包

## 特殊技能包创建

特殊技能包指可实现tts、asr、唤醒等等的技能包。

和普通技能包一样，你同样需要config.json和main.py。

比如TTS功能：

config.json:
```json
{
  "enable": true,
  "funcType": "TTS"
}
```

此外，main.py无需check和main,但必须需要一个函数，用于实现tts功能

以“TTS_BAIDU_API”插件为例：

```python
import model.player
import model.mod_manager

def tts(tts_string):
    # <do something>
    model.player.playsound_from_file('result.mp3')

model.mod_manager.setFunc(tts, "TTS")
```

我们可以看到，最后运行了一个model.mod_manager.setFunc(tts, "TTS")，用于声明“tts”函数为TTS功能

我们定制了两个接口，分别是：

### TTS插件

TTS插件同样有一个参数：text，是要生成的句子

### ASR插件

ASR插件的函数需要有一个参数：path

path是录音文件的路径

不过，有一个插件比较特殊——

### HuanXing唤醒插件

它是不需要注册的，你可以直接将代码放进main，不需要任何函数。

当然，编写唤醒插件有些特殊，所以你需要遵守我们的 唤醒插件编写标准 才可以被收录至ringrobot的插件库

（详见wiki）

## hook 钩子接口

为了方便用户自定义功能，我们开放了hook接口。

您可以使用hook来实现”当说话时，LED灯泡亮“等操作。

下面，就让我们看看hook是怎么使用的：

### HookClient 钩子客户端

```python
from model.hook import *

def tesdef(a):
    print("Hello World Form hook!")
add_hook_fast("RRCore.Main.Before.Running",tesdef)
```

当这个钩子客户端创建 在钩子”RRCore.Main.Before.Running“运行之前时

（也就是当ring启动时），你将会在控制台内看到一条"Hello World Form hook!"的信息。

钩子命名规则详见wiki。

### HookerRegister 钩子创建

```python
from model.hook import *

register_hook_fast("Hello.World.Hook")
# 创建钩子

def tesdef(a):
    print("Hello World Form hook!")
add_hook_fast("RRCore.Main.Before.Running",tesdef)
runhook_fast("Hello.World.Hook",0)
```

当以上代码运行时，您将会在控制台里看到"Hello World Form hook!"

## ASR 语言转文字

model.asr.audioRecorderCallback(语言路径)

## TTS 文字转语音

model.tts.tts(文字)

## Func 语言处理

func是ringrobot最为核心的部分，它完成了从根据字符串选择技能包到执行tts等一系列操作

### run 执行

run(string, ttsexec="tts")

它会遍历一遍所有可以使用的技能包，直到有一个技能包可以管这个字符串

## Config 保持插件设置

它可以保存插件生成的设置到config目录。

```python
import model.config

test=model.config.APPConfig()
test.setModelName(test,"MYTEST")
test.setConfig(test,"MYTEST","txt")
print(test.getConfig(test,"txt"))
```

执行完成后，会在config目录生成MYTEST.txt文件，并在控制台输出MYTEST

# 支持

由于折腾调是个还处于九年义务教育的学生党 ~~还是个鸽子~~ ，本项目可能活跃时间不长，也没有精力、时间、金钱支撑ringrobotx持续开发

欢迎有开发者向这个项目发起pr，这样不仅是对我的鼓励，也是对ringrobotx莫大的支持

此项目并不是只针对树莓派linux开发板，任何架构都可运行

如果你的开发板在此项目中报错，那么我将会尽最大努力帮你解决问题

（并不意味着我会帮你解决一切问题，所有与ringrobotx无关的问题将不受支持）

这个项目花费了我很多的精力和时间，如果这个项目帮助了你，请考虑向我们”赞赏“一下

如果你喜欢这个点子，可以向本项目发起者 折腾调 整一袋白象

[微信捐赠码](https://www.shushi.tech/assets/avatars/wx.png "微信捐赠码")

[支付宝捐赠码](https://www.shushi.tech/assets/avatars/zfb.jpg "支付宝捐赠码")

当然，你也可以向 Lingkong-robot 和 Lingkong-team 的创始人 Epeiuss 和整个团队买一杯咖啡

> 如果您觉得我们的开源软件对你有所帮助，请进入爱发电赞赏我们，给予一些帮助与鼓励，谢谢！！！
戳这里 -> http://afdian.net/@epeiuss

# 未来工作

1. 插件扩展
* 增加各种TTSASR支持
* 实现后台管理
* 实现 HTTP API 接口以及 WebHook 等扩展功能
* 命令行模式增强：禁启用插件、Debug调试某模块功能等等
2. 文档完善
* 使用wiki
* 完善接口等等使用说明
* 完善技能包创建新手教程
3. 生态完善
* 增加各种花里胡哨的插件（功能），可能会作为 fork 版本发布