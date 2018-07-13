import os
import random
import shutil
import re
import time
from server import DBoperator


tot_user_room = DBoperator.countUserInRooms()

i = 0

"""risultato in elements
{
    "bagno": {
        "rock": 10
    },
    "sala": {
        "pop": 5,
        "rock": 5
    }
}
"""
elements = {}
for i in DBoperator.getStatForRoom():
    if elements.get(i[0]) is None:
        elements[i[0]] = {}
    elements[i[0]].update({i[1]: i[2]})

totals = {}
[totals.update({room: count}) for room, count in DBoperator.countUserInRooms()]

for (room2, dict2) in elements.items():
    for (kind2, count2) in dict2.items():
        count3 = count2 * 10 / totals[room2]
        dict2.update({kind2: int(count3)})
print(elements)


"""
for a in tot_user_room:
    j = 0
    for b in tot_user_room:
        print(tot_user_room[i][j])
        j +=1
    room = tot_user_room[i]
    #print(room[i])
    i+=1




k = i
i = 0
for i in range(0, k):
    print("\nfor the " + tot_user_room[i][0] + "\n")
    pop_people = 1
    rock_people = 1
    rb_people = 0
    pop_songs = (pop_people/tot_user_room[i][1])*10
    rock_songs = (rock_people/tot_user_room[i][1])*10
    rb_songs = (rb_people/tot_user_room[i][1])*10

    print("pop songs: " + str(int(pop_songs)))
    print("rock songs: " + str(int(rock_songs)))
    print("rb songs: " + str(int(rb_songs)))
    i+=1
"""
exit(0)

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