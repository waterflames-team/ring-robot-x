# 常见错误
## 运行时

### 我不小心进入了连续对话模式，如何退出？

编辑config/func.json，你会看到：

```json
{"is_updown": true, "updown_funcname": "aaaaa"}
```

将is_updown后面从true改为false即可