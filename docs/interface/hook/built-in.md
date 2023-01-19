# 内置钩子

## "RRCore.Main.Before.Running"

RingRobotX启动时会运行这个钩子。

无参数

## "RRCore.Model.【Before/After】.FuncRunning"

技能运行前会运行RRCore.Model.Before.FuncRunning。

参数：（dict）{"string": [说的话], "ttsexec": [ttsexec]}

技能运行后会运行RRCore.Model.After.FuncRunning。

参数：（dict）{"string": [说的话], "ttsexec": [ttsexec],"return":[插件返回的话]}

## 其他

"RRCore.Model.After.ContinueDisable":连续对话禁用，参数同RRCore.Model.After.FuncRunning

"RRCore.Model.After.ContinueEnable":连续对话禁用，参数同RRCore.Model.After.FuncRunning

"RRCore.Model.Before.TTSRunning":TTS运行前，参数：tts_string（需要合成的文字）

"RRCore.Model.After.TTSRunning":TTS运行后，参数：tts_string（需要合成的文字）

"RRCore.Model.Before.ASRRunning":ASR运行前，参数：fname（需要识别的语音文件路径）

"RRCore.Model.After.ASRRunning":ASR运行后，参数：fname（需要识别的语音文件路径）

"RRCore.FuncPack.Before.WakeUPRunning": 唤醒运行时。

"RRCore.Func.TTS":TTS插件运行函数，见“特殊技能包”

"RRCore.Func.ASR":ASR插件运行函数，见“特殊技能包”

"RRCore.Model.FuncAction":Func运行函数，你可以用它来实现自己的技能运行。用法见ASR