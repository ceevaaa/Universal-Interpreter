import wave
from struct import *

def loadnconvert(filename):
    n = 0
    frames = (0,)
    sound = wave.open(filename,'r')
    while sound.getnframes() > n:
        frames = frames + unpack('h', sound.readframes(1))
        sound.setpos(n)
        n += 100

    sound.close()
    return soundtomorse(frames)