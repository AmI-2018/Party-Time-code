from os import listdir
import sqlite3 as db
DirMusic = "./music/"
#from server import DBoperator as DB
#import sys
#import os
#sys.path.append(os.path.abspath("./server"))
#from DBoperator import *
import DBoperator as DB

def findKind():
    kindOfMusic = list(listdir(DirMusic))
    return kindOfMusic

if __name__ == '__main__':
    #DBinit(DirMusic)
    DB.DBinit(DirMusic)
    rows = DB.showAllMusic()
    for row in rows:
        print(row)

    print(DB.showAllMusic)
    print("music are " + str(findKind()))












































