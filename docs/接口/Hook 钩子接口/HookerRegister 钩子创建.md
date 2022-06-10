
```python
from model.hook import *

register_hook_fast("Hello.World.Hook")
# 创建钩子

def tesdef(a):
    print("Hello World Form hook!")
add_hook_fast("Hello.World.Hook",tesdef)
runhook_fast("Hello.World.Hook",0)
```

当以上代码运行时，您将会在控制台里看到"Hello World Form hook!"
