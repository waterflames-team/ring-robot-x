
# RingRobotX - 好用易开发的语音对话机器人框架

这是一个python语音对话机器人框架，根据LingkongRobot修改而来
特色功能：

1. 模块化管理（技能扩展包，功能扩展包）
2. 技能模块化 - 开发更简单！
3. 我们都喜欢的命令行！你可以通过命令行直接对话！
4. 配置简单化，配置可以在config目录修改，避免直接修改源代码！
5. 实现了连续对话 - 终于可以和机器人玩成语接龙了！
6. 从根部开始重构 - 摆脱LingkongRobotV1的600行文件！
7. 开放，简洁的API接口，您可以迅速入手框架并自定义自己的使用方式！
8. 对于Geek，开放Hook钩子！在任何地方Hook你的函数！

好了，准备好体验激动人心的RingRobot了吗？现在开始！

# 须知

RingRobotX 是lingkongteam成员“zhetengtiao”自行重构，并不在lingkongrobot 2.0重构计划范围内。

请期待lingkongrobot 2.0！

RingRobot Core核心是默认使用pyttsx3进行语音合成的，中文发音比较生硬

您可以自定义tts.py进行修改

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
git clone https://gitee.com/lkteam/ring-robot-x
```

运行此命令后，ring将会下载到命令执行的目录

当然，如果你追求稳定，可以从我们的项目主页下载发行版

如果你追求新功能，请下载develop版本

### 2.安装语音唤醒功能

唤醒功能依赖包：https://github.com/Kitt-AI/snowboy.git

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

# 框架接口
## hook 钩子接口

为了方便用户自定义功能，我们开放了hook接口。

您可以使用hook来实现”当说话时，LED灯泡亮“等操作。

下面，就让我们看看hook是怎么使用的：

### HookClient 钩子客户端

```python
def tesdef(a):
    print("Hello World Form hook!")
testhook=model.hook.HookClient
testhook.hookEverything(testhook,"RRCore.Main.Before.Running",tesdef)
```

当这个钩子客户端创建 在钩子”RRCore.Main.Before.Running“运行之前时

（也就是当ring启动时），你将会在控制台内看到一条"Hello World Form hook!"的信息。

钩子命名规则详见wiki。

### HookerRegister 钩子创建

```python
testhook=model.hook.HookerRegister("Hello.World.Hook")
# 创建钩子

def tesdef(a):
    print("Hello World Form hook!")
testhooka=model.hook.HookClient
testhooka.hookEverything(testhooka,"Hello.World.Hook",tesdef)

testhook.run_Hook(testhook,"Hello.World.Hook")
```

当以上代码运行时，您将会在控制台里看到"Hello World Form hook!"

## Func 语言处理

func是ringrobot最为核心的部分，它完成了从根据字符串选择技能包到执行tts等一系列操作

### run 执行

run(string, ttsexec="tts")

它会遍历一遍所有可以使用的技能包，直到有一个技能包可以管这个字符串

## Config 保持插件设置

它可以保存插件生成的设置到config目录。

```python
test=model.config.APPConfig()
test.setModelName(test,"MYTEST")
test.setConfig(test,"MYTEST","txt")
print(test.getConfig(test,"txt"))
```

执行完成后，会在config目录生成MYTEST.txt文件，并在控制台输出MYTEST
