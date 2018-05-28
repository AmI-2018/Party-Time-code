import sqlite3
import logging
import sys
import os
import glob
from time import sleep

path = "./tmpDB"
musicPath = ""

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.ERROR)

"""
 INSERT INTO `musicDB` (`title`, `kind`) VALUES
      ('havana', 'pop'),
      ('boh', 'rock'),
      ('boh2', 'jazz');
"""


class DBoperator:

    def __init__(self, musicFolder):
        global musicPath
        musicPath = musicFolder
        try:
            con = sqlite3.connect(path)
            cur = con.cursor()

            enableFK = "PRAGMA foreign_keys = ON;"
            cur.executescript(enableFK)
            con.commit()
            query = """
                --DROP TABLE IF EXISTS `music`;
                CREATE TABLE IF NOT EXISTS `music` 
                    (
                      `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                      `title` varchar(200) NOT NULL,
                      `kind` varchar(200) NOT NULL,
                      `location` varchar(200) NOT NULL 
                    );
                --DROP TABLE IF EXISTS `users`;
                CREATE TABLE IF NOT EXISTS `users`
                    (
                      `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                      `username` VARCHAR(200) NOT NULL,
                      `preference1` VARCHAR(200) NOT NULL, 
                      `preference2` VARCHAR(200),
                      `preference3` VARCHAR(200),
                      FOREIGN KEY (username) REFERENCES users(username)
                    );
                    
                --DROP TABLE IF EXISTS `rooms`;
                CREATE TABLE IF NOT EXISTS `rooms`
                    (
                      `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                      `roomName` VARCHAR(200),
                      `raspberryIP` VARCHAR(200),
                      `hueID` VARCHAR(200), 
                      `beaconID` VARCHAR(200),
                      `beaconIDMajor` INTEGER ,
                      `beaconIDMinor` INTEGER                       
                    );   
                --DROP TABLE IF EXISTS `positions`;
                CREATE TABLE IF NOT EXISTS `positions`
                    (
                      `username` VARCHAR(200),
                      `beaconID` VARCHAR(200),
                      `beaconMajor` INTEGER,
                      `beaconMinor` INTEGER,
                      `time` TIMESTAMP, 
                      FOREIGN KEY (username) REFERENCES users(username),
                      FOREIGN KEY (beaconID, beaconMajor, beaconMinor) REFERENCES rooms(beaconID, beaconMajor, beaconMinor)
                    ); 
                """

            cur.executescript(query)
            con.commit()

            cur.close()
            con.close()

        except sqlite3.DataError as DataErr:
            print("errore di creazione table " + DataErr.args[0])
        except sqlite3.DatabaseError as DBerror:
            print("errore nell'apertura del db " + DBerror.args[0])
            sys.exit(1)

    def newTrack(self, trackName, trackPath, trackKind):
        try:
            con = sqlite3.connect(path)
            cur = con.cursor()
            query = """INSERT INTO `music` (`title`, `kind`, `location`) VALUES (?,?,?)"""
            cur.execute(query, (trackName, trackKind, trackPath))
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

    def showAllMusic(self):
        try:
            print("show all music")
            con = sqlite3.connect(path)
            cur = con.cursor()
            query = """select `title`, `kind`, `location` from `music`"""
            cur.execute(query)
            rows = cur.fetchall()
            print("risultati")
            # for row in rows:
            #    print(row)

            cur.close()
            con.close()
        except sqlite3.DataError as DataErr:
            print("errore di creazione table " + DataErr.args[0])
        except sqlite3.DatabaseError as DBerror:
            print("errore nell'apertura del db " + DBerror.args[0])
            sys.exit(1)
        return rows

    def getListByGenre(genre):
        "to be done"
        pass
    def registerUserPosition(self, beacon, major, minor, username):
        try:
            query = """
                INSERT INTO positions (username, beaconID, beaconMajor, beaconMinor, time) 
                VALUES (?,?,?,?,CURRENT_TIMESTAMP);
                """
            con = sqlite3.connect(path)
            cur = con.cursor()

            cur.execute(query, (username, beacon, major, minor))
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


        """
        backup of the old but working version of importMusic()

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

        """
    def createRoom(self, roomName, raspIP, hueID, beaconID, beaconMajor, beaconMinor):
        """create room entry in DB using roomName, ip of raspi, hue id associated, beaconID associated (with major and minor)"""
        try:
            query = """
                INSERT INTO rooms(roomname, raspberryIP, hueID, beaconID, beaconIDMajor, beaconIDMinor)
                VALUES (?,?,?,?,?,?);
                """
            con = sqlite3.connect(path)
            cur = con.cursor()

            cur.execute(query, (roomName, raspIP, hueID, beaconID, beaconMajor, beaconMinor))
            con.commit()
            cur.close()
            con.close()
        except sqlite3.DataError as DataErr:
            print("errore di creazione table " + DataErr.args[0])
        except sqlite3.DatabaseError as DBerror:
            print("errore nell'apertura del db " + DBerror.args[0])
            sys.exit(1)

    def createUser(self, username, preference1, preference2, preference3):
        """Create username in database, need 3 preference, use None if less prefs provided"""

        try:
            query = """
                       INSERT INTO users(username, preference1, preference2, preference3)
                       VALUES (?,?,?,?);
                       """
            con = sqlite3.connect(path)
            cur = con.cursor()

            cur.execute(query, (username, preference1, preference2, preference3))
            con.commit()
            cur.close()
            con.close()
        except sqlite3.DataError as DataErr:
            print("errore di creazione table " + DataErr.args[0])
        except sqlite3.DatabaseError as DBerror:
            print("errore nell'apertura del db " + DBerror.args[0])
            sys.exit(1)

    def importMusic(self):

        # for roots, dirs, files in os.walk("./music"):
        #    print(files)
        # return
        global musicPath
        # xoprint("music path: " + musicPath)
        for roots, dirs, files in os.walk(musicPath):
            # print('roots ', end='')
            # print(roots)
            # print('musicpath ', end='')
            # print(musicPath)
            if (roots != musicPath):
                for track in files:
                    genre = roots.replace(musicPath + '/', '')
                    trackPath = roots + '/' + track
                    self.newTrack(track, trackPath, genre)
                    # print(track + ' ' + trackPath + ' ' + genre)
        # showAllMusic()
        return
    def getKindsOfMusic(self):
        query = "SELECT DISTINCT kind FROM music  "
        try:

            con = sqlite3.connect(path)
            cur = con.cursor()

            cur.execute(query)
            rows = cur.fetchall()
            print("risultati " + str(rows))
            con.commit()
            cur.close()
            con.close()
        except sqlite3.DataError as DataErr:
            print("errore di creazione table " + DataErr.args[0])
        except sqlite3.DatabaseError as DBerror:
            print("errore nell'apertura del db " + DBerror.args[0])
            sys.exit(1)

if __name__ == '__main__':
    db = DBoperator("./music")
    db.importMusic()
    db.createUser("ciccio", "rock", "pop", None)
    db.registerUserPosition("1234", "1111", "2222", "ciccio")
    db.createRoom("sala", "10.0.0.1", "3429872347", "1234", "1111", "2222")
    # db.getKindsOfMusic()
    # DBinit("./music")
    # importMusic()
    # print(showAllMusic())
