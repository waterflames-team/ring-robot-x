# HookerRegister 钩子创建

```python
from model.hook import *

register_hook_fast("Hello.World.Hook")
# 初始化钩子

def tesdef(a):
    print("Hello World Form hook!")
add_hook_fast("Hello.World.Hook",tesdef)# 将函数添加进钩子
runhook_fast("Hello.World.Hook",0)# 运行钩子
```

当以上代码运行时，您将会在控制台里看到"Hello World Form hook!"
