# Ask the user for the number of years
years = int(input("How many years would you like to calculate the rainfall for?"))
# A variable to track the total inches of rain fall
total_rainfall = 0.0
# A variable to store the total number of months
total_months = years*12
# Loop through each year
for year in range(1, years+1):
    # Loop through each month in each year
    for month in range(1, 13):
        rainfall = float(input(f"How many inches of rain fell in month number {month}? "))
        # Add up the total raingfall as each month is entered
        total_rainfall+= rainfall
        
# Figure out the average rainfall and save it to a variable
average_monthly_rainfall = total_rainfall/total_months

# Display the required information
print(f"Number of months: {total_months}")
print(f"Total inches of rainfall for the {years}: {total_rainfall}")
print(f"Average rainfall per month: {average_monthly_rainfall:.2f}")