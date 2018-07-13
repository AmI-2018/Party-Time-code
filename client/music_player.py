import os, random, time, sys

import pygame

mp3s = []
mediapath = "playlist"


for path, directory, element in os.walk(mediapath, False):
    print("Loading music from" + path + "...")
    tmparray = element

    for i in range(0, len(tmparray) - 1):
        #if (tmparray[i][-3:] == "m4a" and tmparray[i][:1] != "."):
        mp3s.append(tmparray[i])
        print(tmparray[i])
        #else:
            #print("Unuseable:", tmparray[i])

    print("Loaded" + str(len(mp3s)) + "files, of" + str(len(element)) + "total")

random.shuffle(mp3s)



for i in range(0, len(tmparray) - 1):
    pygame.mixer.init()
    tmpString = mediapath + '/' + mp3s[i]
    print(mp3s[i])
    print(tmpString)
    pygame.mixer.music.load(mp3s[i])
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

"""
for i in range(0, len(tmparray) - 1):
    print(mp3s[i])
    os.system(mediapath + mp3s[i] + "'")
    time.sleep(1)
"""