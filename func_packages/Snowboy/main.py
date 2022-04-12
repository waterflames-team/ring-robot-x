import model.hook
import func_packages.Snowboy.snowboymain

model.hook.add_hook_fast("RRCore.Main.Before.Running",func_packages.Snowboy.snowboymain.run())