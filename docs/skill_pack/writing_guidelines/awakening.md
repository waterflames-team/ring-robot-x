# 唤醒

## 注意事项

由于RingRobotX引入软件包的特性，所以：

* 你需要尽量不堵塞主线程，或者hook到"RRCore.Main.Before.Running"（见特殊技能包）

否则，可能会进入“整个程序都在等着你”的尴尬局面

另外，

* 你需要在当录音时（detectedCallback）执行以下代码：
```python
model.hook.runhook_fast("RRCore.FuncPack.Before.WakeUPRunning",0)# hook运行
model.player.playsound_from_file(os.path.split( os.path.realpath( sys.argv[0] ) )[0]+"/"+'assets/music/ding.wav')# 播放唤醒提示音
```

* 哦对了，录音完成后调用 model.asr.audioRecorderCallback(录音文件路径)

（实例详见snowboy插件