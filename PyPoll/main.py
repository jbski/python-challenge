import os
import csv



# Get the path to the csv file
csvpath = os.path.join("Resources", "election_data.csv")

#Open the csv file
with open(csvpath) as election_datafile:

    csvreader = csv.reader(election_datafile, delimiter=",")
    #Exclude the header row
    csv_header = next(csvreader)

# Convert the csv file data to a python object
    election_data = list(csvreader)

    # Create an empty list to hold the unique candidate names and total names
    candidate_names = []
    names = []
    names_all = []
    vote_pct = []
    vote_per_candidate = []

    #Get the number of records in the election data 
    upper_range = len(election_data)
    
    #Define and initialize variables
    total_votes = 0

    #Loop through the election data and get variable values
    for i in range(upper_range):

        #Count the total votes
        total_votes +=1

        #Create a candidate name list for counting purposes
        names.append(election_data[i][2])

        #Create a list to keep track of unique candidate info
        if election_data[i][2] not in candidate_names:
            candidate_names.append(election_data[i][2])

    total_candidates = len(candidate_names)

    #Create a list containing the values for candidate, vote percentage, and total votes per candidate
    for j in range(total_candidates):
        names_all.append(candidate_names[j])
        vote_pct.append((names.count(candidate_names[j]) / total_votes) * 100)
        vote_per_candidate.append(names.count(candidate_names[j]))

    #Create a dictionary to help get the winner
    election_dict = dict(zip(names_all, vote_pct))

    winner = max(election_dict, key=election_dict.get)
    
    #Print the results to the terminal
    print(f'\nElection Results')
    print(f'-----------------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'-----------------------------------')
                
    for j in range(total_candidates):
        print(f'{candidate_names[j]}: {(names.count(candidate_names[j]) / total_votes) * 100:.3}%  ({names.count(candidate_names[j])})')

    print(f'-----------------------------------')
    print(f'Winner: {winner}')
    print(f'-----------------------------------\n')

    #Write the results to an output file
    csv_save_path = os.path.join("analysis", "election_data_output.csv")

    analysis_results_output = open(csv_save_path, mode = "w", newline="")

    csv_writer = csv.writer(analysis_results_output, delimiter=',')

    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["-----------------------------------"])
    csv_writer.writerow([f'Total Votes: {total_votes}'])
    csv_writer.writerow(["-----------------------------------"])
    for j in range(total_candidates):
        csv_writer.writerow([f'{candidate_names[j]}: {(names.count(candidate_names[j]) / total_votes) * 100:.3%}  ({names.count(candidate_names[j])})'])

    csv_writer.writerow(["-----------------------------------"])

    csv_writer.writerow([f'Winner: {winner}'])
    csv_writer.writerow(["-----------------------------------"])
    
    







