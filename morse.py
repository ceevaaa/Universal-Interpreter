import sys
import morsealf
import playmorse
import sound

def convtomorse(word,morse):
    strpos = 0
    while strpos <= len(word) - 1:
        morse = morse + morsealf.signtomorse(arg[strpos])
        strpos += 1
    morse = morse + "  " #end of word
    return morse

def finalconversion(seq):
    morse = ""
    morse = convtomorse(seq,morse)
    playmorse.morsetosound(morse)
    print(morsecode.strip())
