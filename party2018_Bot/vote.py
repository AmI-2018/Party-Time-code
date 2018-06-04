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
users_percentage = {"pop": int(users["pop"]/total_users), "rock": int(users["rock"]/total_users),
                    "classic": int(users["classic"]/total_users)}
print("songs percentage multiply by "+str(total_users))
print((str(users_percentage["pop"]*playlist_length)) + " " +
      (str(users_percentage["rock"]*playlist_length)) + " " +
      (str(users_percentage["classic"]*playlist_length)))
