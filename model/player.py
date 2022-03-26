from playsound import playsound
import os

def dele(fpath):
    if os.path.exists(fpath):
        os.remove(fpath)

def playsound_from_file(file):
    playsound(file)