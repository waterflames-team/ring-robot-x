# 特殊技能包

**请在观看本页面前先了解“入前须知”**

特殊技能包指可实现tts、asr、唤醒等等的技能包。

和普通技能包一样，你同样需要config.json、setup.py和main.py。

比如TTS功能：

config.json:
```json
{
  "enable": true,
  "funcType": "TTS",
  "version": "1",
  "apiVersion": "Beta.3"
}
```

此外，main.py无需check和main,但必须需要一个函数，用于实现tts功能

以“baidutts”插件为例：

```python
import model.player
import model.mod_manager

def tts(tts_string):
    # <do something>
    model.player.playsound_from_file('result.mp3')

model.hook.add_hook_fast("RRCore.Func.TTS",tts) # 添加自己的tts函数实现到rrx系统中
```

我们可以看到，最后将tts函数钩在了"RRCore.Func.TTS"里，用于声明“tts”函数为TTS功能

我们定制了两个接口，分别是：

### TTS插件

TTS插件需要将你的tts功能实现函数 hook 到 "RRCore.Func.TTS"

并且tts函数必须只能有一个参数，用来传入需要转为语音的文字

### ASR插件

同样要挂到钩子："RRCore.Func.ASR"

ASR插件的函数需要有一个参数，这是录音文件的路径

不过，有一个插件比较特殊——

### WakeUP唤醒插件

它是不需要注册的，你可以直接将代码放进main.py里，不需要任何函数。

此外，为了不堵塞前台程序运行，你可以试着使用多线程等等，如果必须要主线程，那么可以这么做：

1. 将你的唤醒实现封装到一个函数里
2. 将这个函数挂到"RRCore.Main.Before.Running"这个钩子里

当然，编写唤醒插件有些特殊，所以你需要遵守我们的 唤醒插件编写标准（另见编写指北） 才可以被收录至ringrobot的插件库
