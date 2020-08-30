import os
import csv


# def analyze_fin_data(findata):
#     financials = list(findata)
#     print(len(financials))
    

    
        



# * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

    

# get the path to the csv file
csvpath = os.path.join("Resources", "budget_data.csv")
# csvpath = "C:/Gitlab/python-challenge/PyBank/Resources/budget_data.csv"


# # read the csv file and store in a variable
with open(csvpath) as csvfile:

    findata = csv.reader(csvfile, delimiter=",")
    csv_header = next(findata)

    financials = list(findata)
    print(len(financials))
    # print(financials)

    pnl = []

    for num in financials:
        pnl.append(int(num[1]))

    total_pnl = sum(pnl)
    print(total_pnl)

    max_pnl = max(pnl)

    

    
    

