import os
import csv


# get the path to the csv file

csvpath = os.path.join("..", "Resources", "budget_data.csv")



# read the csv file and store in a variable
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    # csv_header = next(csvreader)

    for row in csvreader:
        print(row)