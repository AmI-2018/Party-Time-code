import DBoperator as DB
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
    print(sorted_list)





