import os
import csv


# * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# Get the path to the csv file
csvpath = os.path.join("Resources", "election_data.csv")

#Open the csv file
with open(csvpath) as election_datafile:

    csvreader = csv.reader(election_datafile, delimiter=",")
    #Exclude the header row
    csv_header = next(csvreader)

# Convert the csv file data to a python object
    election_data = list(csvreader)
    election_header = list(csv_header)

    # print(election_header)
    # print(election_data[0])

    # Create an empty list to hold the unique candidate names and related values
    candidate_info = []

    #Get the number of records in the election data
    upper_range = len(election_data)
    
    #Define and initialize variables
    total_votes = 0

    #Loop through the election data and get variable values
    for i in range(upper_range):

        total_votes +=1

        if election_data[i][2] not in candidate_info:
            candidate_info.append(election_data[i][2])

        
    print(f'Election Results')
    print(f'-----------------------------------')
    print(f'Total Votes {total_votes}')
    
    total_candidates = len(candidate_info)
    for i in range(total_candidates):
        print(f'{candidate_info[i]} :')

    # print(candidate_info)
    









# Read the csv