"""
prototype used for vote_function version 2

"""

import operator

def vote():

    kinds = ["rock", "pop", "rb"]  # initialize list
    total_user_per_room=[('bagno',10),('sala',20)] # initialize rooms

    user_per_genre=[{'rock':3,'pop':5,'rb':2},{'rock':14,'pop':3,'rb':3}]
    print(kinds)
    print(total_user_per_room)
    print(user_per_genre)
    return user_per_genre


if __name__ == '__main__':
    kinds = ["rock", "pop", "rb"]  # initialize list
    playlist = vote()
    for j in range(0,2):
        for i in range(0,3):
            print(kinds[i], playlist[j][kinds[i]])

"""import DBoperator as DB
import operator

def vote():

    N=20 #number of songs per playlist

    kinds=["rock","pop","rb"]  #initialize list
    user_per_genre=[]  #initialize list
    playlist={} #empty dictionary

    total_users = DB.countUserInRooms() #number of users in a specific room

    for i in range(0,2):
       user_per_genre[i] = DB.countUserInRoomByGenre(kinds[i]) #users of kind[i] present in a specific room

    for i in range(0,3):
       playlist[kinds[i]] = int(float(user_per_genre[i])/float(total_users)*N)
        #with the playlist now we have to play songs based on the playlist

    return playlist

#create a folder with playlist characteristics and pass the directory to ftp.py

if __name__ == '__main__':
    playlist = vote()
    sorted_list = sorted(playlist.items(), key=operator.itemgetter(1),reverse=True)
    print(sorted_list)"""