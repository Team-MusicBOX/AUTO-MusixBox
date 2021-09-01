from multiprocessing import Process
import pyglet

path = 'C:/DevSpace/capstone2/music/'
c = path + 'do.mp3'
d = path + 're.mp3'
g = path + 'sol.mp3'
a = path + 'la.mp3'
b = path + 'si.mp3'

def playDo():
    song = pyglet.media.load(c)
    song.play()

def playRe():
    song = pyglet.media.load(d)
    song.play()

def playSol():
    song = pyglet.media.load(g)
    song.play()

def playLa():
    song = pyglet.media.load(a)
    song.play()

def playSi():
    song = pyglet.media.load(b)
    song.play()


def makeProcess(list):
    newList = []
    for i in range(len(list)):
        if list[i] == 0:
            newList.append(Process(target=playDo()))
        elif list[i] == 1:
            newList.append(Process(target=playRe()))
        elif list[i] == 2:
            newList.append(Process(target=playSol()))
        elif list[i] == 3:
            newList.append(Process(target=playLa()))
        elif list[i] == 4:
            newList.append(Process(target=playSi()))

    return newList


