# CLI

## Console

```python
import model.cli

a = model.cli.console

print(a.commandRun(a,"help","tts"))
```

会输出“help tts”命令的运行结果

## 命令

```python
"hook":"hook [runmode] [hookname] | runmode可输入reg或run，分别代表初始化hook列表和运行hook",
"func":"func [string] | 输入你想对RingRobotX说的话。",
"tts":"tts [string] | 运行tts ===== asr [path] | 运行asr",
"asr":"tts [string] | 运行tts ===== asr [path] | 运行asr",
"help":"help (command) 获取（某一指令的）帮助",
"hello":"彩蛋。",
"clear":"clear [log/history] | 清除记录（history需要插件RingRobotX_ChatHistory插件支持）",
"check-update":"check-update | 检查更新，OK为可更新，No为不可更新",
"update":"update | 更新程序",
"config":"config [list/get/set] 配置名 扩展名 解码 值(仅当set时可用) | 列出、获取、设置配置文件。\n 例如：config list（列出） \n config get Turing_RobotChat（获取） \n config set Turing_RobotChat json utf-8 {}（设置）"
```

详细请运行RingRobotX并在CLI中输入help。