import DBoperator as db

def vote():
    N = 20  # number of songs per playlist
    kinds = ["rock", "pop", "rb"]  # initialize list
    rooms = ["bagno","sala"] #rooms
    total_users = db.countUserInRooms()
    print(total_users)
    users_per_gen = {}
    for i in range (0,3):
        users_per_gen [kinds[i]] = db.countUserInRoomByGenre(kinds[i])
        print(users_per_gen)
    playlist={
        rooms[0]: [N, 0, 0],
        rooms[1]: [0, N, 0],
    }
    id_songs=[[],[]]
    for i in range (0,N):
        id_songs[0].append(i+1)
        id_songs[1].append(i+66)
    print(playlist)
    print(id_songs)
    return id_songs

if __name__ == '__main__':
    playlistids=vote()
    """
    
    the vote function return a playlist with each rows indicating a room and each column indicating
    an id of a song present in the database  
    
    """



