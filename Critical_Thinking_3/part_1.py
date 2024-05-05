meal_cost = float(input("What was the cost of the meal without the tip, or tax included?"))
tax = float(meal_cost*0.07)
tip = float(meal_cost*0.18)

print("The tax for your",meal_cost,"meal was",tax)
print("The tip for your",meal_cost,"meal was", tip)
print("The total cost for your meal was",float(meal_cost)+float(tip)+float(tax))