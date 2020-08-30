import os
import csv



#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

    

# get the path to the csv file
csvpath = os.path.join("Resources", "budget_data.csv")



# # read the csv file and store in a variable
with open(csvpath) as csvfile:

    findata = csv.reader(csvfile, delimiter=",")
    csv_header = next(findata)

    financials = list(findata)

# print(financials)

upper_range = len(financials)
max_pnl_increase = 0
max_pnl_decrease = 0
total_months = 0
total_pnl = 0
pnl_change_total = 0
pnl_change_count = 0
pnl_change = 0
pnl_change_lst = []
j = 0
print(financials)
for i in range(0,upper_range):
    pnl_change_2 = int(financials[i][1])
    pnl_change_1 = int(financials[i-1][1])
    pnl_change = pnl_change_2 - pnl_change_1
    total_months +=1
    total_pnl += int(financials[i][1])

    pnl_change_lst.append(pnl_change)

    if pnl_change > max_pnl_increase:
        max_pnl_increase = pnl_change
        max_pnl_date = str(financials[i][0])

    if pnl_change < max_pnl_decrease:
        max_pnl_decrease = pnl_change
        min_pnl_date = str(financials[i][0])
    
print(pnl_change_lst)
total_pnl_change = sum(pnl_change_lst)
total_pnl_change_count = len(pnl_change_lst)
avg_change = total_pnl_change / total_pnl_change_count

print(str(total_months))
print(str(total_pnl))
print(str(avg_change))
print(max_pnl_date, str(max_pnl_increase))
print(min_pnl_date, str(max_pnl_decrease))



#create dictionary for pnl calculations
monthly_change_date = []
monthly_change_pnl = []


upper_range = len(financials)
for i in range(1,upper_range):
    pnl_date = str(financials[i][0])
    monthly_change_date.append(pnl_date)        
    

for i in range(1,upper_range): 
    pnl_change_2 = int(financials[i][1])
    pnl_change_1 = int(financials[i-1][1])
    pnl_change = pnl_change_2 - pnl_change_1
    monthly_change_pnl.append(int(pnl_change))


stats_dict = dict(zip(monthly_change_date, monthly_change_pnl))

total_pnl_values = 0
num_values = 0
max_value = 0

for value in stats_dict.values():
    total_pnl_values += value
    num_values += 1

    if value > max_value:
        max_value = value
        


avg_change = total_pnl_values / num_values


# print("Dictionary: " + str(avg_change))






    

    
    

