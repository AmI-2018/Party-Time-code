"""

this is just an idea of the voting system which should be a proportional
compilation of a playlist

"""


print("hello")
genres = ["pop", "rock", "classic"]
users = {"pop": 6, "rock": 9, "classic": 1}
print("write the length of the playlist u want to create:...")
playlist_length = int(input())
# try a number smaller , bigger and equal to total users

total_users = users["pop"]+users["rock"]+users["classic"]
print("total users are " + str(total_users))
users_percentage = {"pop": float(users["pop"])/float(total_users), "rock": float(users["rock"])/float(total_users),
                    "classic": (float(users["classic"])/float(total_users))}
print("songs percentage multiply by "+str(playlist_length))
print((str(int(users_percentage["pop"]*playlist_length))) + " " +
      (str(int(users_percentage["rock"]*playlist_length))) + " " +
      (str(int(users_percentage["classic"]*playlist_length))))
