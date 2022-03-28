from pydub import AudioSegment
from pydub.playback import play
import os

def dele(fpath):
    if os.path.exists(fpath):
        os.remove(fpath)

def playsound_from_file(file):
    song = AudioSegment.from_wav(file)
    play(song)