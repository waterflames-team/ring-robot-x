![banner](docs/photo/banner.png)

# 写在开头

这是一个python语音对话机器人，根据Lingkong-Robot重构而来

可用于智能音箱，语言遥控，甚至智能客服、家庭管家、微信机器人等等

目的是让中国的 Maker 们也能够「一小时」入门，无需过多以及不必要的配置

特色功能：

1. 技能包具有较强的灵活性，可随意支配技能
2. 命令窗口直接对话
3. 配置简单化，配置可以在config目录修改，避免直接修改源代码
4. 实现了连续对话 - 终于可以和机器人玩成语接龙了
5. 开放，简洁的接口，接入简单
6. 高度可自定义
7. 开放的HTTP接口，让你的应用程序快速接入RingRobotX框架！

好了，准备好体验 RingRobotX 了吗？现在开始！

# 须知

RingRobotX 是 LingKongRobot 的重构版本

RingRobotX默认（git仓库版本）内置图灵、百度ASR&TTS、snowboy唤醒插件

（是的即使snowboy停止维护了但是还能耍

在线模型训练：https://snowboy.hahack.com/

感谢wzpan老师的网站）

# 入门 （第一次尝试RingRobotX）

[戳我](https://rrx.lkteam.cn/#/%E6%96%B0%E6%89%8B%E5%85%A5%E9%97%A8 "Wiki")

# 安装

## 方案1：自动安装脚本

自动安装脚本只支持使用apt的linux发行版（如debian，ubuntu等等），建议你使用清华软件源

若您要使用稳定版本，请运行：
```shell
wget -O install.sh https://gitee.com/lkteam/ring-robot-x/raw/master/install.sh && sudo bash install.sh
```

若您要使用测试版本，请运行：
```shell
wget -O install.sh https://gitee.com/lkteam/ring-robot-x/raw/develop/install.sh && sudo bash install.sh
```

>**安装程序会安装到脚本执行目录/ringrobotx/ring-robot-x**

当然，如果你是其他发行版（或者一键安装脚本有错误），可以试着第二种方案：手动安装。

## 方案2：手动安装

### 1.安装RingRobotX

```shell
sudo apt install python3 python3-pip git python3-pyaudio swig libatlas-base-dev pulseaudio make alsa-utils sox libsox-fmt-mp3
mkdir ringrobotx && cd ringrobotx
git clone https://gitee.com/lkteam/ring-robot-x
cd ring-robot-x
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

运行此命令后，ring将会下载到命令执行的目录

当然，如果你追求稳定，可以从我们的项目仓库下载发行版或直接下载master分支的内容

如果你追求新功能，请下载develop分支的内容

### 2.安装语音唤醒功能

>**PS：若您不准备使用snowboy功能，那么可以跳过此步，并将下载的项目目录/func_packages/Snowboy/config.json中“"enable": ”后面的true改为false**

唤醒功能依赖[snowboy](https://github.com/Kitt-AI/snowboy.git)

为了避免某些问题，snowboy暂时不会集成到ringrobotx

所以，我们需要手动安装snowboy

请执行以下命令：

```shell
git clone https://github.com/Kitt-AI/snowboy.git
cd snowboy/swig/Python3
make
cd ../../../
cp snowboy/swig/Python3/_snowboydetect.so ring-robot-x/func_packages/Snowboy
cp snowboy/examples/Python3/snowboydetect.py ring-robot-x/func_packages/Snowboy
cp -a snowboy/resources/ ring-robot-x/func_packages/Snowboy/resources
cd ../
```

# 运行

```shell
cd ringrobotx/ring-robot-x
python3 ring.py
```

内置的模型唤醒词是“灵空灵空”，不同设备上录音会有不同效果，建议在自己设备上训练效果更好

你可以替换掉，模型文件在config/snowboy/model.pmdl

# web后台

运行后，程序默认会在本地的8901端口开启一个后台

用户名随意，密码在第一次启动会随机设置，请留意控制台输出

你可以修改密码、端口号在/config/RingRobotX_Web.json中

# 设置

详见config目录下的各种json文件

如果你需要禁用某一插件，那么到func_packages/插件名/config.json的enable改为false即可

# Wiki

[戳我](https://rrx.lkteam.cn/ "Wiki")

# 遇到问题

[戳我](https://gitee.com/lkteam/ring-robot-x/issues "Issues")创建一个issue

# 支持

由于LKT的小伙伴们还是处于九年义务教育的学生党们 ~~还是群鸽子~~ ，所以本项目可能不会经常活跃

欢迎有开发者向这个项目发起pr，这样不仅是对LKT的鼓励，也是对ringrobotx莫大的支持

此项目并不是只针对树莓派linux开发板，任何架构都（可能）可以运行

如果你的开发板在此项目中报错，那么我将会尽最大努力帮你解决问题

这个项目花费了我们很多的精力和时间，如果您觉得我们的开源软件对你有所帮助，可以向 LingKongTeam 的创始人 Epeiuss 和整个团队多整几袋白象,戳这里 -> [http://afdian.net/@epeiuss](http://afdian.net/@epeiuss)

# 二次开发

如果你准备将其闭源并商业使用，那么请确认你知晓 LingKongTeam 不为任何使用了二次分发软件的 安全性，可用性，完整性 以及其可能带来的 其它风险及损失 承担责任。

其余或有冲突之处以 Apache License 2.0 开源协议为准

另外，本项目不受 LingKongRobot 的 GPL 协议影响。

# 特别感谢

* wzpan 本项目借鉴了 wukong-robot 项目的一部分基本底层代码 & snowboy训练网站（wukong-robot是个好项目！
* 本项目的前身 lingkong-robot
