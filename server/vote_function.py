import DBoperator as DB

def vote(roomName):

    N=10 #number of songs per playlist
    rows=DB.getKindsOfMusicAndCount()

    kinds=[rock,pop,jazz]  #initialize list
    print(kinds)
    user_per_genre=[]  #initialize list
    playlist={} #empty dictionary

    for kind,count in rows :
        kinds.append(kind)

    print(kinds)
    total_users = DB.countTotalUser()

    for i in range(0,total_users):
        user_per_genre[i] = DB.countUser(kinds[i])

    for i in range(0,total_users):
        playlist[kinds[i]] = float(user_per_genre[i])/float(total_users)*N

    return playlist



