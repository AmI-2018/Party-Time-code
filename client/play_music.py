import os, random, time, sys
import time
import pygame
import json

if __name__ == '__main__':

    #mp3s = set()
    mp3s = {}
    folder = './playlist'
    abspath = os.path.abspath(folder)
    #print(abspath)
    #exit()
    for path, directory, elements in os.walk(abspath):
        #print(element)
        for element in elements:
            if element not in mp3s.keys():
                mp3s[path + '/' + element] = 0
            #print()
            #print(i)
            #mp3s.add(path + '/' + i)
        #exit()
    #random.shuffle(mp3s)

    print(json.dumps(mp3s, indent=4, sort_keys=False))
    exit()

    for mp3 in mp3s.keys():
        try:
            pygame.mixer.init()
            print('carico: ' + mp3)
            pygame.mixer.music.load(str(mp3))
            print('riproduco: ' + mp3 + ' per la ' + mp3s[mp3] + ' volta')
            mp3s[mp3] = mp3s[mp3] + 1
            pygame.mixer.music.play()


            """
            while pygame.mixer.music.get_busy() == True:
                time.sleep(0.2)
            """
            time.sleep(5)
        except KeyboardInterrupt:
            pass
        except pygame.error as message:
            print('doh')
            print(message)
            mp3s[mp3] = -1
            pass
        finally:
            pygame.mixer.stop()






