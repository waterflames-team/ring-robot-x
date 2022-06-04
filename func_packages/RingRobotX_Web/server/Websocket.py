import asyncio
import base64
import threading
import traceback
import bcrypt
import model.config
import websockets
import model.cli

console=model.cli.console()
async def hello(websocket, path):
    while True:
        command = await websocket.recv()
        global console

        command=str(base64.b64decode(command), "utf-8")

        clist = command.split()
        try:
            command1 = clist[1]
            password=clist[0]
            clist.pop(0)
            clist.pop(0)
        except:
            model.logger.moduleLoggerMain.info("[CLI-Server] 报告！您的命令无法解析。"+command)
            model.logger.moduleLoggerMain.info(traceback.format_exc())
            back="[CLI-Server] 报告！您的命令无法解析。"
            await websocket.send(back)

        if not bcrypt.checkpw(model.config.fastGetConfig("RingRobotX_Web")["password"].encode(), password.encode()):
            model.logger.moduleLoggerMain.info("[CLI-Server] 报告！您的token错误，请尝试刷新网页以生成新token"+password)
            back = "[CLI-Server] 报告！您的token错误，请尝试刷新网页以生成新token"+password
            await websocket.send(back)
            return

        back=str(base64.b64encode(str(console.commandRun(command1, tuple(clist))).encode()), "utf-8")
        await websocket.send(back)

def run():
    start_server = websockets.serve(hello, '', model.config.fastGetConfig("RingRobotX_Web")["websocket_port"])
    asyncio.get_event_loop().run_until_complete(start_server)
    threading.Thread(target=asyncio.get_event_loop().run_forever).start()
    model.logger.moduleLoggerMain.info("[CLI-Server] CLI-Server启动。")
