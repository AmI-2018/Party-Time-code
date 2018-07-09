import os, random, time, sys
import glob
from pygame import mixer # Load the required library
import pygame
import time
from mutagen.mp3 import MP3
#import mpg123
from pygame import mixer # Load the required library
#from mpg123 import Mpg123

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

pygame.init()
"""
for i in range(0, len(tmpArray)-1):
    print(mp3s[i])
    os.system(mediapath + '\\' + mp3s[i])
"""

for i in range(0, len(tmpArray)-1):
    tmpString = "./" + mediapath + '/' + mp3s[i]
#    print(mp3s[i])
    print(tmpString)
    pygame.mixer.music.load(tmpString)
    #pyg.mixer.music.load(tmpString)
# instantiate pygame
#    pygame.init()

# select track
    #pygame.mixer.music.load(tmpString)
 #   len = MP3(tmpString).info.length
    print("riproduco: " + tmpString)
#    pygame.mixer.music.play()
    time.sleep(5)

#    time.sleep(len-1)

# play music (on loop)
    pygame.mixer.music.play(-1, 0.0)

# wait
#    time.sleep(10)

# stop music
#    pygame.mixer.music.stop()
