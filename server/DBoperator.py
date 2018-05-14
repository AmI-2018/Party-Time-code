import sqlite3
import logging
import sys
import os
import glob
from time import sleep

path = "./tmpDB"
musicPath = "./music"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.ERROR)


"""
 INSERT INTO `musicDB` (`title`, `kind`) VALUES
      ('havana', 'pop'),
      ('boh', 'rock'),
      ('boh2', 'jazz');
"""
def DBinit():

    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        query = """
DROP TABLE IF EXISTS `musicDB`;
    CREATE TABLE IF NOT EXISTS `musicDB` 
(
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `title` varchar(200) NOT NULL,
  `kind` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL 
);
     
        """
        cur.executescript(query)
        con.commit()
        #cur.execute("select  * from musicDB")
        #rows = cur.fetchall()
        #print("risultati " + str(rows))
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)

def newTrack(trackName, trackPath, trackKind):
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        query = """INSERT INTO `musicDB` (`title`, `kind`, `location`) VALUES (?,?,?)"""
        cur.execute(query, (trackName, trackPath, trackKind))
        con.commit()
        # cur.execute("select  * from musicDB")
        # rows = cur.fetchall()
        # print("risultati " + str(rows))
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)
def showAllMusic():
    try:
        print("show all music")
        con = sqlite3.connect(path)
        cur = con.cursor()
        query = """select `title`, `kind`, `location` from `musicDB`"""
        cur.execute(query)
        rows = cur.fetchall()
        print("risultati")
        for row in rows:
            print(row)
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)

def importMusic():

    for roots, dirs, files in os.walk("./music"):
        pass
    for roots, dirs, files in os.walk(musicPath):
        if(roots != musicPath):
            for track in files:
                genre = roots.replace(musicPath + '/', '')
                trackPath = roots + '/' + track
                newTrack(track, trackPath, genre)
    showAllMusic()
    return


if __name__ == '__main__':
    DBinit()
    importMusic()