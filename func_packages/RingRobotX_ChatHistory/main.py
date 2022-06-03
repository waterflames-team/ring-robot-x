import model.hook
import model.cli

history=[]

def add_history(message):
    global history
    history.append({"que":message["string"],"ans":message["return"]})

def get_history():
    global history
    return history

model.hook.add_hook_fast("RRCore.Model.After.FuncRunning",add_history)
model.cli.command_registry("history",get_history)
model.cli.help_registry("history","history | 输出记录到的对话记录")