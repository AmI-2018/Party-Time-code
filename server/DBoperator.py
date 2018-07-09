import sqlite3
import logging
import sys
import os

path = "./.tmpDB"
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
'''
    todo funcion which return number of total users and number of
    users for each preference.
    countTotalUser() return number of all users
    countUsers(kindOfMusic) return users with kindOfMusic as parameter kindOfMusic is a string
'''
def countTotalUser():

def initialize(musicFolder):
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
                  `preference3` VARCHAR(200)--,
                  --FOREIGN KEY (username) REFERENCES users(username)
                );

            --DROP TABLE IF EXISTS `rooms`;
            #hueID is the light name 
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


def newTrack(trackName, trackPath, trackKind):
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


def showAllMusic():
    try:
        print("show all music")
        con = sqlite3.connect(path)
        cur = con.cursor()
        query = """SELECT DISTINCT `title`, `kind`, `location` from `music`"""
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

def getListOfUsers():
    query = "select username from users ORDER BY username;"
    print("this is returned by the DBoperator")
    return customQueryWithReturn(query)

def removeUser(username):
    query = "delete from users WHERE username like ?;"
    ret = customQueryWithReturnOneParameter(query, username)
    return ret

def registerUserPosition(beacon, major, minor, username):
    try:
        query = """
            INSERT INTO positions (username, beaconID, beaconMajor, beaconMinor, time)
            VALUES (?,?,?,?,CURRENT_TIMESTAMP);
            """
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute(query, (str(username), str(beacon), str(major), str(minor)))
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


def createRoom(roomName, raspIP, hueID, beaconID, beaconMajor, beaconMinor):
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


def createUser(username, preference1, preference2, preference3):
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


def importMusic():
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
                newTrack(track, trackPath, genre)
                # print(track + ' ' + trackPath + ' ' + genre)
    # showAllMusic()
    return


def getKindsOfMusic():

    """ Return a list of all kinds of music avaible in the DB """
    query = "SELECT DISTINCT kind FROM music  "
    rows = ""
    try:

        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute(query)
        rows = cur.fetchall()
        print("risultati " + str(rows))
        print(type(rows))
        con.commit()
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)
    return rows

def getKindsOfMusicAndCount():

    """ Return a list of all kinds of music avaible in the DB """
    query = "select kind, count(*) from music GROUP BY kind"
    rows = ""
    try:

        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute(query)
        rows = cur.fetchall()
        print("risultati " + str(rows))
        print(type(rows))
        con.commit()
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)
    return rows


def clearDB():
    query = """
            DROP TABLE IF EXISTS `music`;
            DROP TABLE IF EXISTS `positions`;
            DROP TABLE IF EXISTS `rooms`;
            DROP TABLE IF EXISTS `users`;
            """
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.executescript(query)
        con.commit()
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)


def userInDB(username):
    query = "select username from users where username like ?"
    try:
        ret = False
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(query, (username,))
        rows = cur.fetchall()
        if len(rows) > 0:
            ret = True

        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)
    return ret


def createExampleEntries():
    importMusic()
    createUser("ciccio", "rock", "pop", None)
    createUser("baciccio", "jazz", "rock", None)
    createUser("tizio", "r&b", "jazz", None)
    createUser("caio", "house", "pop", "classica")
    registerUserPosition("1234", "1111", "2222", "ciccio")
    # createRoom("sala", "10.0.0.1", "3429872347", "1234", "1111", "2222")
    createRoom("sala", "10.0.0.3", "83972732", "B9407F30-F5F8-466E-AFF9-25556B57FE6D", "24156", "10712")
    createRoom("bagno", "10.0.0.36", "8397232732", "B9407F30-F5F8-466E-AFF9-25556B57FE6D", "27390", "29386")

def beaconsList():
    query = "select DISTINCT roomName, beaconID, beaconIDMajor, beaconIDMinor from rooms"
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) <= 0:
            ret = false
        else:
            ret = rows
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)
    return ret

def customQueryWithReturn(query):
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)
    return rows

def customQueryWithReturnOneParameter(query, param1):
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(query, param1)
        rows = cur.fetchall()
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)
    return rows

if __name__ == '__main__':
    # clearDB()
    # initialize("./music")
    # createExampleEntries()
    # print(userInDB("ciccio"))
    # print(userInDB("ale"))
    # print(showAllMusic())
    # getKindsOfMusicAndCount()
    # db.getKindsOfMusic()
    # DBinit("./music")
    # importMusic()
    # print(showAllMusic())

    print(getListOfUsers())
