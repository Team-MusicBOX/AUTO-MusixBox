from multiprocessing import Process
import playNotes as np

def playMusic(finalPosition):
    for i in finalPosition:
        play_list = []
        play_list = np.makeProcess(i)
        print(play_list)
        if __name__ == '__main__':
            for j in play_list:
                j.start()
                j.join()