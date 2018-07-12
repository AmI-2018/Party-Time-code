import os, random, time, sys
import time
import pygame


if __name__ == '__main__':

    mp3s = set()
    folder = './playlist'
    abspath = os.path.abspath(folder)
    #print(abspath)
    #exit()
    for path, directory, element in os.walk(abspath):
        #print(element)
        for i in element:
            #print()
            #print(i)
            mp3s.add(path + '/' + i)
        #exit()
    #random.shuffle(mp3s)


    for mp3 in mp3s:
        pygame.mixer.init()
        print('carico: ' + mp3)
        pygame.mixer.music.load(str(mp3))
        print('riproduco: ' + mp3)
        pygame.mixer.music.play()
        try:
            """
            while pygame.mixer.music.get_busy() == True:
                time.sleep(0.2)
            """
            time.sleep(5)
        except KeyboardInterrupt:
            pass
        except pygame.error:
            pass
        finally:
            pygame.mixer.stop()
            





