它可以保存插件生成的设置到config目录。

```python
import model.config

test=model.config.APPConfig()
test.setModelName(test,"MYTEST")
test.setConfig(test,"MYTEST","txt")
print(test.getConfig(test,"txt"))
```

执行完成后，会在config目录生成MYTEST.txt文件，并在控制台输出MYTEST