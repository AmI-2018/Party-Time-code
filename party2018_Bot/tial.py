"""
prototype used for vote_function

"""

import operator

def vote():
    N = 100  # number of songs per playlist

    kinds = ["rock", "pop", "jazz"]  # initialize list
    print(kinds)

    user_per_genre = [9,3,1]  # initialize list
    playlist = {}  # empty dictionary
    total_users = 3+9+1

    for i in range(0, 3):
        playlist[kinds[i]] = int(float(user_per_genre[i]) / float(total_users) * N)

    return playlist

if __name__ == '__main__':
    playlist=vote()
    sorted_list = sorted(playlist.items(), key=operator.itemgetter(1),reverse=True)
    print(sorted_list)