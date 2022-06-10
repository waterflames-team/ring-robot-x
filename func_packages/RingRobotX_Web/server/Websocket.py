import asyncio
import base64
import json
import threading
import traceback
import bcrypt
import model.config
import websockets
import model.cli
import model.hook
from types import FunctionType
import func_packages.RingRobotX_Web.main
import nest_asyncio

nest_asyncio.apply() #修复asyncio在listen_hook时的特性

hook_client={}

console=model.cli.console()

def pat_hook(web_key,hook,param):
    global hook_client
    print("Hook listened. "+web_key+" hook: "+hook)
    asyncio.run(hook_client[web_key].send(str(base64.b64encode(str(hook+" "+json.dumps(param)).encode()), "utf-8")))

async def hello(websocket, path):
    while True:
        command = await websocket.recv()
        global console
        global hook_client

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

        if command1 == "listen-hook":

            if not clist[0] in model.hook.HookList.keys():
                await websocket.send("W0NMSS1TZXJ2ZXJdIOS4u+WKqOmYsuaKpOagoemqjOaLpuaIqu+8muacquaJvuWIsGhvb2vlkI3miJZob29r5ZCN5LiN5ZCI5rOV")
                continue

            web_key=func_packages.RingRobotX_Web.main.getRandom(5)
            hook_client[web_key]=websocket
            func_name='CLIServer_Websocket_listen_hook_'+func_packages.RingRobotX_Web.main.getRandom(5)
            print('def '+func_name+'(*param): asyncio.run(pat_hook("'+web_key+'","'+clist[0]+'",param))')
            foo_code = compile('def '+func_name+'(*param): pat_hook("'+web_key+'","'+clist[0]+'",param)', "<string>", "exec")
            foo_func = FunctionType(foo_code.co_consts[0], globals(), func_name)
            model.hook.add_hook_fast(clist[0],foo_func)
            await websocket.send("T0s=")
            continue

        back=str(base64.b64encode(str(console.commandRun(command1, tuple(clist))).encode()), "utf-8")
        await websocket.send(back)

def run():
    start_server = websockets.serve(hello, '', model.config.fastGetConfig("RingRobotX_Web")["websocket_port"])
    asyncio.get_event_loop().run_until_complete(start_server)
    threading.Thread(target=asyncio.get_event_loop().run_forever).start()
    model.logger.moduleLoggerMain.info("[CLI-Server] CLI-Server启动。")
