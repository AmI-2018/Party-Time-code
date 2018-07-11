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
    for j in range (0,len(rooms)):
        for i in range (0,len(kinds)):
           playlist[len(rooms)][len(kinds)]=

if __name__ == '__main__':
    vote()



