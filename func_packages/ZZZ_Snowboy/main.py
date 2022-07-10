import model.hook
import func_packages.ZZZ_Snowboy.snowboymain

model.hook.add_hook_fast("RRCore.Main.Before.Running",func_packages.ZZZ_Snowboy.snowboymain.run)
