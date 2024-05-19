# Ask the user 
books = int(input("How many books did you purchase this month?"))

# Figure out how many points the user earned this month based on how many books they purchased
# for this I am going to use if else statements 
if books == 0 or books == 1:
    points = 0
elif books == 2 or books == 3:
    points = 5
elif books == 4 or books == 5:
    points = 15
elif books == 6 or books == 7:
    points = 30
elif books >= 8:
    points = 60

print(f"This month you have earned {points} points")