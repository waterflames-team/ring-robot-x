# HTTP API

## history 对话历史（需要ChatHistory插件）

参数：无

路径：/history

方式：get

返回示例：

```json
{"code": 0, "message": "ok", "history": "[{\"que\": \"\\u65f6\\u95f4\", \"ans\": \"\\u65f6\\u95f4\\u5411\\u524d\\u6c79\\u6d8c\\u4e0d\\u56de\\u5934\"}]"}
```

history: 数据

que：用户提问

ans：机器人回答

## Chat 对话

路径：/chat

方式：post

参数：query：说的话

返回：无。