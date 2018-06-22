import os, random, time, sys
import glob
from pygame import mixer # Load the required library

mp3s = []
mediapath = "playlist"


for path, directory, element in os.walk(mediapath, False):
    print("Loading music from " + path + "...")
    tmparray = element

    for i in range(0, len(tmparray)):
        if (tmparray[i][-3:] == "mp3" and tmparray[i][:1] != "."):
            mp3s.append(tmparray[i])
        else:
            print("Unuseable:", tmparray[i])

    print("Loaded " + str(len(mp3s)) + " files, of " + str(len(element)) + " total")

print(mp3s)
random.shuffle(mp3s)

#prima opzione
for i in range(0, len(tmparray)):
    print(mp3s[i])
    os.system("mpg123 '" + mediapath + mp3s[i] + "'")
    time.sleep(1)

