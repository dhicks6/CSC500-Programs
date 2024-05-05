current_time = input("What is the current time in 24 hour format?")
alarm = input("How many hours would you like to set the alarm for?")
## Using modulo here to get the time the alarm will go off
time_after_alarm = (int(current_time)+int(alarm))%24
## If the time_after_alarm is 0
if(time_after_alarm == 0):
    print("The alarm will go off at 00:00")
## If time after alarm is < 10 we need to add a 0 to the front
elif(time_after_alarm < 10):
    print("The alarm will go off at 0" + str(time_after_alarm) + ":00")
## If time alarm is >= 0
else:
    print("The alarm will go off at " + str(time_after_alarm) + ":00")