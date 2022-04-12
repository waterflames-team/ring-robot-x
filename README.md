# RingRobotX - 灵活易开发的对话机器人框架

这是一个python语音对话机器人框架，根据Lingkong-Robot重构而来

可用于智能音箱，语言遥控，甚至智能客服、家庭管家、微信机器人等等

目的是让中国的 Maker 们也能够「一小时」入门，无需过多以及不必要的配置

特色功能：

1. 技能包具有较强的灵活性，可随意支配技能
2. 命令窗口直接对话
3. 配置简单化，配置可以在config目录修改，避免直接修改源代码
4. 实现了连续对话 - 终于可以和机器人玩成语接龙了
5. 开放，简洁的接口，接入简单
6. 没有复杂死板的封装
7. 高度可自定义
8. （TODO）开放的HTTP接口，让你的应用程序快速接入RingRobotX框架！

好了，准备好体验 RingRobotX 了吗？现在开始！

# 须知

RingRobotX 是 LingKongRobot 的重构版本

RingRobotX默认（git仓库版本）内置图灵、百度ASR&TTS、snowboy唤醒插件

（是的即使snowboy死了但是还能耍

在线模型训练：https://snowboy.hahack.com/

感谢wzpan老师的网站）

# 安装

## 方案1：自动安装脚本

自动安装脚本只支持使用apt的linux发行版（如debian，ubuntu等等），建议你使用清华软件源

运行：
```shell
wget -O install.sh https://gitee.com/lkteam/ring-robot-x/raw/develop/install.sh && sudo bash install.sh
```

当然，如果你是其他发行版（或者一键安装脚本有错误），可以试着第二种方案：手动安装。

## 方案2：手动安装

### 1.安装RingRobotX

```shell
sudo apt install python3 python3-pip git python3-pyaudio swig libatlas-base-dev pulseaudio make alsa-utils
pip3 install pydub playsound
git clone https://gitee.com/lkteam/ring-robot-x
```

运行此命令后，ring将会下载到命令执行的目录

当然，如果你追求稳定，可以从我们的项目仓库下载发行版

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
python3 ~/ringrobotx/ring-robot-x/ring.py
```

哦对了，内置的模型唤醒词是“灵空灵空”

你可以替换掉，它在assets/snowboy/model.umdl

# 设置

详见config目录下的各种json文件

你需要：百度语音apikey，图灵apikey

如果你需要禁用某一插件，那么到func_packages/插件名/config.json的enable改为false即可

# Wiki

[戳我](https://gitee.com/lkteam/ring-robot-x/wikis "Wiki")

# 遇到问题

[戳我](https://gitee.com/lkteam/ring-robot-x/issues "Issues")创建一个issue

# 支持

由于折腾调是个还处于九年义务教育的学生党 ~~还是个鸽子~~ ，本项目可能活跃时间不长，也没有精力、时间、金钱支撑ringrobotx持续开发

欢迎有开发者向这个项目发起pr，这样不仅是对我的鼓励，也是对ringrobotx莫大的支持

此项目并不是只针对树莓派linux开发板，任何架构都可运行

如果你的开发板在此项目中报错，那么我将会尽最大努力帮你解决问题

这个项目花费了我很多的精力和时间，如果这个项目帮助了你，请考虑向我们”赞赏“一下

如果你喜欢这个点子，可以向本项目发起者 折腾调 整一袋白象

[微信捐赠码](https://www.shushi.tech/assets/avatars/wx.png "微信捐赠码")

[支付宝捐赠码](https://www.shushi.tech/assets/avatars/zfb.jpg "支付宝捐赠码")

当然，你也可以向 LingKongTeam 的创始人 Epeiuss 和整个团队买一杯咖啡

> 如果您觉得我们的开源软件对你有所帮助，请进入爱发电赞赏我们，给予一些帮助与鼓励，谢谢！！！
戳这里 -> http://afdian.net/@epeiuss

# 未来工作

1. 插件扩展
* 增加各种TTSASR支持
* 实现后台管理
* 实现 HTTP API 接口等扩展功能
* 命令行模式增强：禁启用插件、Debug调试某模块功能等等

# 二次开发

你可以下载代码后自由修改/查看代码。

当然，如果你准备将其闭源并商业使用，那么请遵守：
1. 请确认你知晓 LingKongTeam 不为任何使用了二次分发软件的 安全性，可用性，完整性 以及其可能带来的 其它风险及损失 承担责任。
2. 如果你修改了 RingRobotX ，那么请在被修改的文件中注明——即使没人会去看它。
3. 你 **必须** 在你的程序内注明代码来源，比如 “使用了开源免费的 RingRobotX ”

其余或有冲突之处以 Apache License 2.0 开源协议为准

另外，本项目不受 LingKongRobot 的 GPL 协议影响。

# 感谢

* wzpan 本项目借鉴了 wukong-robot 项目的一部分基本框架设计 & snowboy训练网站（wukong-robot是个好项目！
* 本项目的前身 lingkong-robot
