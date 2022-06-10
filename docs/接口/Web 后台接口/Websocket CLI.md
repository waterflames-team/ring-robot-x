连接端口设置位于RingRobotX_Web配置中。

默认地址：ws://localhost:8902/

首先，你需要获取到RingRobotX_Web配置中的密码，然后使用bcrypt进行加密。这就是token。

然后，当连接到Websocket后：

如果你要输入一个“hello”命令给服务器，那么你需要这么操作：

1. 将上文你获取到的token与命令以一个空格隔开，如：“kejfefjhejbhfbh hello”，其中kejfefjhejbhfbh就是我们的token
2. 将第一步得到的字符串进行base64编码，发送至服务器。
3. 当收到服务器的响应时，你需要将服务器发送的字符串进行base64解码，才能获得服务器返回的信息。