from server import DBoperator

kindOfMusic = DBoperator.getKindsOfMusicAndCount()
print(kindOfMusic)

N=10 #number of songs per playlist
rows=DBoperator.getKindsOfMusicAndCount()

kinds=[]  #initialize list
user_per_genre=[]  #initialize list
playlist={} #empty dictionary

for kind,count in rows :
    kinds.append(kind)

print(kinds)
total_users=DBoperator.countTotalUser()

for i in range(0,total_users):
    user_per_genre[i]=DBoperator.countUser(kinds[i])

for i in range(0,total_users):
    playlist[kinds[i]]=float(user_per_genre[i])/float(total_users)*N
