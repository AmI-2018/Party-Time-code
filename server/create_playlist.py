import os
import random
import shutil
import re
from server import DBoperator
import json
from ftplib import FTP
import os
import time

while True:
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
    #print(elements)

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


    music_base = os.path.abspath('./music')
    basedir = os.path.abspath('./playlist')
    to_be_sent = {}

    for room3, dic in elements.items():
        """
        playlist_dir = os.path.join(basedir,room3)
        if not os.path.exists(playlist_dir):
            os.makedirs(playlist_dir)
            for f in os.listdir(playlist_dir):
                os.remove(playlist_dir)
        """

        tmp = []
        tmp.clear()

        for genre, nSongs in elements[room3].items():
            tmp.extend(DBoperator.getNSongsByGenre(nSongs, genre))

        #print("sending to: " + room3)
        #[print(ir) for ir in tmp]
        #print()
        #print()

        to_be_sent[room3] = tmp
    #    print(to_be_sent)
    #print(json.dumps(to_be_sent, indent=4))
    #[print(DBoperator.getIpByName(rom) for to_be_sent)]
    #exit(0)



    for room in to_be_sent.keys():
        roomIP = DBoperator.getIpByName(room)
        # ftp settings
        server = roomIP
        username = 'dietpi'
        password = 'passwordComplessa'
        remote_path = "/"
        ftp_connection = FTP(server, username, password)
        ftp_connection.cwd(remote_path)
        for music in to_be_sent[room]:
            print('trasferisco: ' + str(os.path.basename(music)) + ' a ' + roomIP)
            fh = open(str(music), 'rb')
            ftp_connection.storbinary('STOR ' + str(os.path.basename(music)), fh)
            fh.close()

    time.sleep(60*20)

