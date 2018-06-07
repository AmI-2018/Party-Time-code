from server import DBoperator

kindOfMusic = DBoperator.getKindsOfMusicAndCount()
print(kindOfMusic)

N=10
kinds=DBoperator.getListByGenre()
numberOfAllUsers=DBoperator.getKindsOfMusicAndCount()
genre=DBoperator.getKindsOfMusic()

for i in range (0,N):
    playlist={genre:genre/numberOfAllUsers*10}
    print(playlist)