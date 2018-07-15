from server import DBoperator

tot_user_room = DBoperator.countUserInRooms()
room = []

print(tot_user_room)
print(tot_user_room[0][0])

exit()

for a in DBoperator.countUserInRooms():
    print(a[0])
    print(a[1])
exit(0)
