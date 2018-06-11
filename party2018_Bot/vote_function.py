from server import DBoperator

kindOfMusic = DBoperator.getKindsOfMusicAndCount()
print(kindOfMusic)

N=10
#kinds=DBoperator.getListByGenre()
numberOfAllUsers=DBoperator.getKindsOfMusicAndCount()
rows=DBoperator.getKindsOfMusicAndCount()
kinds=[]
for kind,count in rows :
    kinds.append(kind)
print(kinds)
'''    
for i in range (0,N):
    playlist={genre:genre/numberOfAllUsers*10}
    print(playlist)
    i++
'''