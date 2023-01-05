# 新手入门
## 系统选择

使用支持apt的系统。（ubuntu，debian等等）

如果是树莓派，那么官方系统（arm，arm64都可以）

## 安装

运行：
```shell
wget -O install.sh https://gitee.com/lkteam/ring-robot-x/raw/develop/install.sh && sudo bash install.sh
```

>**安装程序会安装到脚本执行目录/ringrobotx/ring-robot-x**

## 配置

RingRobotX使用json作为配置语言。

配置在安装目录/config下，那一大堆json就是啦

### baidutts & baiduasr

> ASR TTS引擎

API_KEY 百度语音的API_KEY

SECRET_KEY 百度语言的SECRET_KEY

CUID 随便填

其余不建议更改，可参照百度语言api文档

### Turing_RobotChat
> 图灵机器人（本项目所使用的闲聊功能api）

apikey 图灵机器人apikey

city 你所在的城市

userId 图灵机器人userId

### Clock

> 闹钟

set_time 设置的时间，比如 06:15

playPath 到时间时，播放音乐的路径

### RingRobotX_Web

> web后台

password 密码。

listen_port web后台监听地址

websocket_port websocket后台监听地址（用于CLI通信）

first-load 是否需要随机密码，true是，false否。生成完自动更改为false

## 插件开关

你可以到安装目录/func_packages里面看到许多插件。

一个插件的目录下，会有config.json文件，编辑它

enable 是否启用，true为启用，false为禁用

description 备注

Author 作者

version 版本

其余不建议更改

## 运行

```shell
python3 ./ringrobotx/ring-robot-x/ring.py
```

## web后台

运行后，程序默认会在本地的8901端口开启一个后台

用户名随意，密码在第一次启动会随机设置，请留意控制台输出

## snowboy 模型训练

在线模型训练：https://snowboy.hahack.com/

用你获得到的模型，去替换assets/snowboy/model.umdl文件

## 后台运行

建议使用screen，因为可能需要用到cli。而且程序日志输出可能较多，不建议nohup或&等方式