
def vote(roomName):
    N = 10  # number of songs per playlist

    kinds = [rock, pop, jazz]  # initialize list
    print(kinds)

    user_per_genre = []  # initialize list
    playlist = {}  # empty dictionary
    total_users = DBoperator.countTotalUser()

    for i in range(0, total_users):
        user_per_genre[i] = DBoperator.countUser(kinds[i])

    for i in range(0, total_users):
        playlist[kinds[i]] = float(user_per_genre[i]) / float(total_users) * N
    print(playlist)
    playlistByRoom{roomName }

    return playlist

