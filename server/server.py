from os import listdir
import sqlite3 as db
DirMusic = "./music/"

def findKind():
    kindOfMusic = list(listdir(DirMusic))
    return kindOfMusic

if __name__ == '__main__':

    print("music are " + str(findKind()))












































