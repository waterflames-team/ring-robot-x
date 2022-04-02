from multiprocessing import Process

def main():
    import func_packages.Snowboy.snowboymain

p=Process(target=main,args=())
p.start()