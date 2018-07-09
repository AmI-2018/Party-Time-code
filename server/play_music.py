import os, random, time, sys
import glob
from pygame import mixer # Load the required library
import pygame
import time

import mpg123
from pygame import mixer # Load the required library
from mpg123 import Mpg123

mp3s = []
mediapath = "playlist"


for path, directory, element in os.walk(mediapath, False):
    print("Loading music from " + path + "...")
    tmparray = element

    for i in range(0, len(tmparray)):
        if (tmparray[i][-3:] == "mp3" and tmparray[i][:1] != "."):
            mp3s.append(tmparray[i])
            print(mp3s[i])
        else:
            print("Unuseable:", tmparray[i])

    print("Loaded " + str(len(mp3s)) + " files, of " + str(len(element)) + " total")


random.shuffle(mp3s)

"""
for i in range(0, len(tmparray)-1):
    print(mp3s[i])
    os.system(mediapath + '\\' + mp3s[i])
"""

for i in range(0, len(tmparray)-1):
    print(mp3s[i])
# instantiate pygame
    pygame.init()

# select track
    pygame.mixer.music.load(mediapath + '\\' + mp3s[i])

# play music (on loop)
    pygame.mixer.music.play(-1, 0.0)

# wait
    time.sleep(10)

# stop music
    pygame.mixer.music.stop()

