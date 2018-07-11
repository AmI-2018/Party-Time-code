import os, random, time, sys
import glob
import pygame
import time
#from mutagen.mp3 import MP3
#import mpg123
#from pygame import mixer # Load the required library
#from mpg123 import Mpg123



if __name__ == '__main__':

    mp3s = []
    mediapath = "playlist"


    for path, directory, element in os.walk(mediapath, False):
        print("Loading music from " + path + "...")
        tmpArray = element

        for i in range(0, len(tmpArray)):
            #if (tmpArray[i][-3:] == "m4a" and tmpArray[i][:1] != "."):
            mp3s.append(tmpArray[i])
            print(mp3s[i])
            #else:
            #    print("Unuseable:", tmpArray[i])

        print("Loaded " + str(len(mp3s)) + " files, of " + str(len(element)) + " total")



    random.shuffle(mp3s)

    import pygame

    brano = '/home/ale-dell/Git/Party-Time-code/client/playlist/sejifh wyeyfw8ey8fy we8 yfaow ong.mp3'

    pygame.mixer.init()
    pygame.mixer.music.load(brano)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
"""
    pygame.init()

    for i in range(0, len(tmpArray)-1):
        tmpString = "./" + mediapath + '/' + mp3s[i]
        print(mp3s[i])
        print(tmpString)
        pygame.mixer.music.load(tmpString)
        #pyg.mixer.music.load(tmpString)
        pygame.mixer.music.load(tmpString)
        #   len = MP3(tmpString).info.length
        print("riproduco: " + tmpString)
        pygame.mixer.music.play()
        time.sleep(5)
        pygame.mixer.music.stop()
    #    time.sleep(len-1)

    # play music (on loop)
        #pygame.mixer.music.play(-1, 0.0)
"""