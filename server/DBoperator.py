import sqlite3
import logging
import sys

path = "./tmpDB"

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
  `kind` varchar(200) NOT NULL
);
     
        """
        cur.executescript(query)
        con.commit()
        cur.execute("select  * from musicDB")
        rows = cur.fetchall()
        print("risultati " + str(rows))
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)


if __name__ == '__main__':
    DBinit()