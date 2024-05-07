for i in range(10):
    current_runner = runners[i]
    if current_runner == "Dustin Hicks":
        print(i)
        

current_room_temp = room_temp.read_room_temp
desired_temp = input("What temp would you like to set the room to?")
while current_room_temp != desired_temp:
    room_temp.increase_room_temp(1)