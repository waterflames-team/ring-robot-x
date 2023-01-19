# HookClient 钩子客户端

```python
from model.hook import *

def tesdef(a):
    print("Hello World Form hook!")
add_hook_fast("RRCore.Main.Before.Running",tesdef)
```

当这个钩子客户端创建 在钩子”RRCore.Main.Before.Running“运行之前时

（也就是当ring启动时），你将会在控制台内看到一条"Hello World Form hook!"的信息。
