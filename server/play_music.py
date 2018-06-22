import os, random, time, sys
import glob
from pygame import mixer # Load the required library

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
    os.system("mpg123 '" + mediapath + mp3s[i] + "'")
    time.sleep(1)
"""

for k in range(0, len(tmparray)-1):
    print(mp3s[k])
    mixer.init()
    mixer.music.load(mp3s[k])
    mixer.music.play()
