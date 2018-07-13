import os
import random
import shutil
import re
import time
from server import DBoperator

"""
tot_user_room = DBoperator.countUserInRooms()
room = []
print(tot_user_room)
#print(tot_user_room[0])


i = 0
for j in range(0, len(tot_user_room))
    for a in DBoperator.countUserInRooms():
        room[j] = a[i]
        print(a[i])
        i+=1
exit(0)
print(room)
"""

while True:
    dir = r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist'
    filelist = [f for f in os.listdir(dir) if f.endswith(".mp3")]
    for f in filelist:
        os.remove(os.path.join(dir, f))

    files_pop = os.listdir(os.path.dirname(r'C:\Users\lucag\Desktop\musica\musica nuova\Calvin Harris\Calvin Harris - Funk Wav Bounces Vol.1 [2017]\\'))
    regex = r"(.mp3)"
    pop_people = 3  #here the effective number taken from the DB
    i = 0
    for f in files_pop:
        if i == pop_people:
            break
        if (re.search(regex, f)):
            f = random.choice(files_pop)
            f = os.path.join(r'C:\Users\lucag\Desktop\musica\musica nuova\Calvin Harris\Calvin Harris - Funk Wav Bounces Vol.1 [2017]\\', f)
            shutil.copy(f, r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist')
            i= i+1



    files_rock = os.listdir(os.path.dirname(r'C:\Users\lucag\Desktop\musica\musica nuova\Coldplay\Coldplay - Kaleidoscope EP (2017) (Mp3 320kbps) [Hunter] {786zx}\\'))
    regex = r"(.mp3)"
    rock_people = 5  #here the effective number taken from the DB
    i = 0
    for f in files_rock:
        if i == rock_people:
            break
        if (re.search(regex, f)):
            f = random.choice(files_rock)
            f = os.path.join(r'C:\Users\lucag\Desktop\musica\musica nuova\Coldplay\Coldplay - Kaleidoscope EP (2017) (Mp3 320kbps) [Hunter] {786zx}', f)
            shutil.copy(f, r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist')
            i= i+1


    files_rb = os.listdir(os.path.dirname(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\rb\\'))
    regex = r"(.mp3)"
    rb_people = 2  #here the effective number taken from the DB
    i = 0
    for f in files_rb:
        if i == rb_people:
            break
        if (re.search(regex, f)):
            f = random.choice(files_rb)
            f = os.path.join(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\rb\\', f)
            shutil.copy(f, r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist')
            i= i+1

    from ftplib import FTP
    import os
    import time


    # ftp settings
    settings = {
        'ftp': {
            'url': '192.168.2.34',
            'username': 'dietpi',
            'password': 'passwordComplessa',
            'remote-directory': r'/'
        }
    }

    # local paths
    paths = {
        'local-directory': r'playlist/'
    }
    print(paths['local-directory'])

    # list of local files
    files = os.listdir(paths['local-directory'])
    print(files)

    # connect and store
    for f in files:
        ftp = FTP(settings['ftp']['url'])
        ftp.login(settings['ftp']['username'], settings['ftp']['password'])
        ftp.cwd(settings['ftp']['remote-directory'])
        ftp.storbinary('STOR ' + f, open(paths['local-directory'] + f, 'rb'))
        ftp.close()

    time.sleep(5)