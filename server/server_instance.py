from server.DBoperator import DBoperator

import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

DirMusic = "./music"

if __name__ == '__main__':
    db = DBoperator(DirMusic)
    db.importMusic()
    rows = db.showAllMusic()
    for row in rows:
        print(row)

# print(DB.showAllMusic)
# print("music are " + str(findKind()))
