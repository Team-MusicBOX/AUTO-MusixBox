from multiprocessing import Process
import pyglet
from time import sleep

path = 'C:/Users/ghwt0504/Desktop/music_pi/'
c = path + 'do.mp3'
d = path + 're.mp3'
g = path + 'sol.mp3'
a = path + 'la.mp3'
b = path + 'si.mp3'
c1 = path + 'do1.mp3'
d1 = path + 're1.mp3'
e1 = path + 'mi1.mp3'
f1 = path + 'fa1.mp3'
f1_s = path + 'fa1_s.mp3'
g1 = path + 'sol1.mp3'
g1_s = path + 'sol1_s.mp3'
a1 = path + 'la1.mp3'
a1_s = path + 'la1_s.mp3'
b1 = path + 'si1.mp3'
c2 = path + 'do2.mp3'
c2_s = path + 'do2_s.mp3'
d2 = path + 're2.mp3'
d2_s = path + 're2_s.mp3'
e2 = path + 'mi2.mp3'
f2 = path + 'fa2.mp3'
f2_s = path + 'fa2_s.mp3'
g2 = path + 'sol2.mp3'
g2_s = path + 'sol2_s.mp3'
a2 = path + 'la2.mp3'
a2_s = path + 'la2_s.mp3'
b2 = path + 'si2.mp3'
c3 = path + 'do3.mp3'
d3 = path + 're3.mp3'
e3 = path + 'mi3.mp3'


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

def playDo1():
    song = pyglet.media.load(c1)
    song.play()

def playRe1():
    song = pyglet.media.load(d1)
    song.play()

def playMi1():
    song = pyglet.media.load(e1)
    song.play()

def playFa1():
    song = pyglet.media.load(f1)
    song.play()

def playFa1_s():
    song = pyglet.media.load(f1_s)
    song.play()

def playSol1():
    song = pyglet.media.load(g1)
    song.play()

def playSol1_s():
    song = pyglet.media.load(g1_s)
    song.play()

def playLa1():
    song = pyglet.media.load(a1)
    song.play()

def playLa1_s():
    song = pyglet.media.load(a1_s)
    song.play()

def playSi1():
    song = pyglet.media.load(b1)
    song.play()

def playDo2():
    song = pyglet.media.load(c2)
    song.play()

def playDo2_s():
    song = pyglet.media.load(c2_s)
    song.play()

def playRe2():
    song = pyglet.media.load(d2)
    song.play()

def playRe2_s():
    song = pyglet.media.load(d2_s)
    song.play()

def playMi2():
    song = pyglet.media.load(e2)
    song.play()

def playFa2():
    song = pyglet.media.load(f2)
    song.play()

def playFa2_s():
    song = pyglet.media.load(f2_s)
    song.play()

def playSol2():
    song = pyglet.media.load(g2)
    song.play()

def playSol2_s():
    song = pyglet.media.load(g2_s)
    song.play()

def playLa2():
    song = pyglet.media.load(a2)
    song.play()

def playLa2_s():
    song = pyglet.media.load(a2_s)
    song.play()

def playSi2():
    song = pyglet.media.load(b2)
    song.play()

def playDo3():
    song = pyglet.media.load(c3)
    song.play()

def playRe3():
    song = pyglet.media.load(d3)
    song.play()

def playMi3():
    song = pyglet.media.load(e3)
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
        elif list[i] == 5:
            newList.append(Process(target=playDo1()))
        elif list[i] == 6:
            newList.append(Process(target=playRe1()))
        elif list[i] == 7:
            newList.append(Process(target=playMi1()))
        elif list[i] == 8:
            newList.append(Process(target=playFa1()))
        elif list[i] == 9:
            newList.append(Process(target=playFa1_s()))
        elif list[i] == 10:
            newList.append(Process(target=playSol1()))
        elif list[i] == 11:
            newList.append(Process(target=playSol1_s()))
        elif list[i] == 12:
            newList.append(Process(target=playLa1()))
        elif list[i] == 13:
            newList.append(Process(target=playLa1_s()))
        elif list[i] == 14:
            newList.append(Process(target=playSi1()))
        elif list[i] == 15:
            newList.append(Process(target=playDo2()))
        elif list[i] == 16:
            newList.append(Process(target=playDo2_s()))
        elif list[i] == 17:
            newList.append(Process(target=playRe2()))
        elif list[i] == 18:
            newList.append(Process(target=playRe2_s()))
        elif list[i] == 19:
            newList.append(Process(target=playMi2()))
        elif list[i] == 20:
            newList.append(Process(target=playFa2()))
        elif list[i] == 21:
            newList.append(Process(target=playFa2_s()))
        elif list[i] == 22:
            newList.append(Process(target=playSol2()))
        elif list[i] == 23:
            newList.append(Process(target=playSol2_s()))
        elif list[i] == 24:
            newList.append(Process(target=playLa2()))
        elif list[i] == 25:
            newList.append(Process(target=playLa2_s()))
        elif list[i] == 26:
            newList.append(Process(target=playSi2()))
        elif list[i] == 27:
            newList.append(Process(target=playDo3()))
        elif list[i] == 28:
            newList.append(Process(target=playRe3()))
        elif list[i] == 29:
            newList.append(Process(target=playMi3()))

    return newList

class ThreadMaker:
    def playMusic(finalPosition):
        for i in finalPosition:
            play_list = []
            play_list = makeProcess(i)
            print(play_list)
            if __name__ == '__main__':
                for j in play_list:
                    j.start()
                for j in play_list:
                    j.join()
            sleep(0.51)
