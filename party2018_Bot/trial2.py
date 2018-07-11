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
