import pygame

class Sound:
    short   = 0
    long    = 1
    silence = 2

def playmorse(sound):
    if sound == Sound.short:
        pygame.mixer.music.load("sounds/morse_short.wav")
    elif sound == Sound.long:
        pygame.mixer.music.load("sounds/morse_long.wav")
    elif sound == Sound.silence:
        pygame.mixer.music.load("sounds/silenceshort.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        game = ""

def morsetosound(morsecode):
    pygame.mixer.pre_init(44100, -16, 2)
    pygame.init()
    strpos=0
    while strpos <= len(morsecode) - 1:
        if morsecode[strpos] == ".":
            playmorse(Sound.short)
        elif morsecode[strpos] == "_":
            playmorse(Sound.long)
        else:
            playmorse(Sound.silence)
        strpos += 1

pygame.quit()
