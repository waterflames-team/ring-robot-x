<p align="center">
    <a href="https://docs.waterflames.cn/"><img src="./docs/photo/banner.png" alt="RingRobotX | A Chinese Modular Speech Robot Framework Using Single-Wheel Dialogue Design"></a>
    <br>
    <a href='https://gitee.com/waterflames-team/ring-robot-x/stargazers'><img src='https://gitee.com/waterflames-team/ring-robot-x/badge/star.svg?theme=gvp' alt='star'></img></a>
    <a href='https://gitee.com/waterflames-team/ring-robot-x/members'><img src='https://gitee.com/waterflames-team/ring-robot-x/badge/fork.svg?theme=gvp' alt='fork'></img></a>
    <br>
    <a href="/README.md">中文</a> | <a href="https://docs.waterflames.cn/">Documentation</a> | <a href="https://gitee.com/waterflames-team/ring-robot-x">Gitee</a> | <a href="https://github.com/waterflames-team/ring-robot-x">Github</a> | <a href="https://github.com/waterflames-team/ring-robot-x/discussions">Discussions</a>
    <br>
</p>

# Write at the beginning

This is a Chinese modular voice bot framework designed with a single round of dialogue, made in Python by the WaterFlames team and refactored from our project [Lingkong-Robot](https://github.com/waterflames-team/lingkong-robot).

It can be used for smart speakers, language remote control, and even smart customer service, family butler, WeChat robot, etc.

The goal is to allow even ‘Maker’ to get started in "one hour" without excessive and unnecessary configuration.

Featured features:

1. skill package with strong flexibility to dispose of skills at will.
2. direct dialogue in the command window.
3. configuration simplicity, configuration can be modified in the config directory, to avoid direct modification of the source code.
4. continuous dialogue, finally you can play idiom solitaire with the robot.
5. open, simple interface, easy to access.
6. highly customizable.
7. open HTTP interface, let your application quickly access RingRobotX framework!

Okay, ready to experience RingRobotX? Start now!

# Must know

RingRobotX is a refactored version of [Lingkong-Robot](https://github.com/waterflames-team/lingkong-robot)

RingRobotX by default (git repository version) has built-in Turing, Baidu ASR&TTS, and snowboy wakeup plugins

(Yes, even though snowboy is no longer maintained, it can still be played)

Online model training: https://snowboy.hahack.com/

Thanks to Mr. wzpan for his website)

# Getting Started

## Installation
This project currently supports linux environment for the time being

### Option 1: Auto-install script

The automatic installation script only supports linux distributions that use apt (such as debian, ubuntu, etc.), and it is recommended that you use Tsinghua Software Source

If you want to use a stable version, please run.
```shell
wget -O install.sh https://gitee.com/waterflames-team/ring-robot-x/raw/master/install.sh && sudo bash install.sh
```

If you want to use a test version, run.
```shell
wget -O install.sh https://gitee.com/waterflames-team/ring-robot-x/raw/develop/install.sh && sudo bash install.sh
```

>** The installer will install to the script execution directory /ringrobotx/ring-robot-x**

Of course, if you are on another distribution (or the one-click install script has errors), you can try the second option: manual installation.

### Option 2: Manual installation

#### 1. Install RingRobotX

```shell
sudo apt install python3 python3-pip git python3-pyaudio swig libatlas-base-dev pulseaudio make alsa-utils sox libsox-fmt-mp3
mkdir ringrobotx && cd ringrobotx
git clone https://gitee.com/waterflames-team/ring-robot-x
cd ring-robot-x
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

After running this command, ring will be downloaded to the directory where the command was executed

Of course, if you are looking for stability, you can download the distribution from our project repository or download the master branch directly

If you are looking for new features, please download the development branch

#### 2. Install the voice wakeup feature

>**PS: If you are not going to use the snowboy feature, then you can skip this step and change true to false* after ""enable":" in the downloaded project directory /func_packages/ZZZ_Snowboy/config.json *

Wake-up function depends on [snowboy](https://github.com/Kitt-AI/snowboy.git)

To avoid some problems, snowboy will not be integrated into ringrobotx for now

So, we need to install snowboy manually

Please execute the following command.

```shell
git clone https://github.com/Kitt-AI/snowboy.git
cd snowboy/swig/Python3
make
cd ... /... /... /...
cp snowboy/swig/Python3/_snowboydetect.so ring-robot-x/func_packages/ZZZ_Snowboy
cp snowboy/examples/Python3/snowboydetect.py ring-robot-x/func_packages/ZZZ_Snowboy
cp -a snowboy/resources/ ring-robot-x/func_packages/ZZZ_Snowboy/resources
cd ... /
```

#### Install the skill package manager

```shell
pip3 install mariner-rrx #The following command needs to be run in the directory where RingRobotX is installed
marx install web #Install the admin backend
marx install chathistory #Manage backend dependencies
```

Mariner-RRX is a skill manager that we have prepared for RingRobotX with the command marx. See [marx](https://gitee.com/waterflames-team/mariner) for details

## Run

**The first run after installation will automatically initialize the skills, please wait a little while**

```shell
cd ringrobotx/ring-robot-x
python3 ring.py
```

The built-in model wake-up word is "Lingkong Lingkong", the recording will have different effects on different devices, it is recommended to train on your own device for better results

You can replace it, the model file in config/snowboy/model.pmdl

## web backend

After running, the program will open a backend on local port 8901 by default

User name is random, password will be set randomly in the first start, please pay attention to the console output

You can change the password and port number in /config/RingRobotX_Web.json

## Settings

See the various json files in the config directory for details

If you need to disable a plugin, then go to func_packages/plugin_name/config.json and change enable to false

For more on getting started [poke me for the documentation](https://docs.waterflames.cn/ "Wiki")

# Contact

If you encounter a problem, or have a good suggestion, feel free to contact us at

- You can choose [poke me](https://gitee.com/waterflames-team/ring-robot-x/issues "Issues") to create an issue
- You can also contact us via email: [hi@waterflames.cn](mailto:hi@waterflames.cn)
- Or join the user group via [the following method](https://www.yuque.com/epeiuss/xykong/contact?singleDoc#)

# Secondary Development

If you are prepared to close the source and use it commercially, then please make sure you know that WaterFlames is not responsible for the security, availability, integrity, and other risks and losses that may result from any use of the secondary distribution software.

The Apache License 2.0 Open Source Agreement governs any remaining or conflicting terms.

In addition, this project is not subject to LingKongRobot's GPL license.

# Code Contribution

We welcome every creator to contribute to the open source project. Each contributor is welcome to create a pr and contribute to the project according to the [Submission Information Specification](https://www.yuque.com/epeiuss/xykong/rule?singleDoc#)!

Thanks to every contributor!

# Special thanks to

* wzpan (This project borrows part of the basic underlying code from the wukong-robot project & snowboy training site. wukong-robot is really a superb project!)
* The predecessor of this project, lingkong-robot, and its creator, Epeiuss



> The English version is translated using DeepL, any errors are welcome to be pointed out.

> This project only supports Chinese language use.