import os
import csv


# get the path to the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# read the csv file and store in a variable
with open(csvpath) as csvfile:

    findata = csv.reader(csvfile, delimiter=",")
    csv_header = next(findata)

    financials = list(findata)

# Initialize the required variables - set to 0
max_pnl_increase = 0
max_pnl_decrease = 0
total_months = 0
total_pnl = 0
pnl_change_total = 0
pnl_change_count = 0
pnl_change = 0

# Set the upper range based on the number of rows in the financials list
upper_range = len(financials)

# Loop through each row in the financials data set and assign values to variables
for i in range(0,upper_range):
    pnl_change_2 = int(financials[i][1])
    pnl_change_1 = int(financials[i-1][1])
    pnl_change = pnl_change_2 - pnl_change_1
    total_months +=1
    total_pnl += int(financials[i][1])

    # Skip the first line as there is no entry to calculate change
    # Calculate the change in profit/loss from month to month and get the average
    if i > 0:
        pnl_change_total += pnl_change
        pnl_change_count += 1
        avg_change = pnl_change_total / pnl_change_count
    
    # Find the greates monthly increase in profit/loss
    if pnl_change > max_pnl_increase:
        max_pnl_increase = pnl_change
        max_pnl_date = str(financials[i][0])

    # Find the greatest monthly decrease in profit/loss
    if pnl_change < max_pnl_decrease:
        max_pnl_decrease = pnl_change
        min_pnl_date = str(financials[i][0])
    

#Print the results to the terminal
print("\nFinancial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${str(total_pnl)}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {max_pnl_date} (${max_pnl_increase:.0f})")
print(f"Greatest Decreasee in Profits: {min_pnl_date} (${max_pnl_decrease:.0f})\n")









    

    
    

