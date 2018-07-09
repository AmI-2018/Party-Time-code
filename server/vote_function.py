import DBoperator as DB

def vote():

    N=20 #number of songs per playlist

    kinds=[rock,pop,jazz]  #initialize list
    user_per_genre=[]  #initialize list
    playlist={} #empty dictionary

    total_users = DB.countTotalUser() #number of users in a specific room

    for i in range(0,3):
        user_per_genre[i] = DB.countUser(kinds[i]) #users of kind[i] present in a specific room

    for i in range(0,3):
        playlist[kinds[i]] = int(float(user_per_genre[i])/float(total_users)*N)
        #with the playlist now we have to play songs based on the playlist

    return playlist

#create a folder with playlist characteristics and pass the directory to ftp.py



