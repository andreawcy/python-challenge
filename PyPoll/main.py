import csv
import os

# get the path to the current file
current_dir = os.path.dirname(__file__)

# the path to the CSV file
election_csv = os.path.join(current_dir , 'Resources' , 'election_data.csv')

# list to store data
Candidate = []
Vote = []
Vote_Candidate = []
No_vote_Candidate = []
Vote_rate = []

# Open and read the CSV file 
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Store header row
    header = next(csvreader)

# Start to read from the 2nd row and store the variables
    for row in csvreader:

        # Add vote
        Vote.append(str(row[2]))
   

    # Count total vote
    Total_vote = len(Vote)

    # create unique candidate list and assign 0 to each vote count by candidate
    for item in Vote:
        if item not in Vote_Candidate:
            Vote_Candidate.append(item)
            No_vote_Candidate.append(int(0))
            Vote_rate.append(int(0))
    
    winner_vote = 0

    #count vote by each candidate and assign winner
    for i in range (Total_vote):
        for j in range (len(Vote_Candidate)):
            if (Vote[i] == Vote_Candidate[j]):
                No_vote_Candidate[j] = int(No_vote_Candidate[j])+1
                Vote_rate[j] = round((No_vote_Candidate[j]/Total_vote)*100, 3)
            if No_vote_Candidate[j] > winner_vote:
                winner = j
                winner_vote = No_vote_Candidate[j]
            
                

     # Store the result to a list for printing
    analysis = [
        f"Election Results",
        f"----------------------------",
        f"Total Votes: {Total_vote}",
        f"----------------------------"
        ]
    
    for k in range (len(Vote_Candidate)):
            analysis.append(f"{Vote_Candidate[k]}: {Vote_rate[k]}% ({No_vote_Candidate[k]})")
        
    analysis.append(f"----------------------------")
    analysis.append(f"Winner: {Vote_Candidate[winner]}")
    analysis.append(f"----------------------------")
        

   
   
# print result to a new txt file    
result_path = os.path.join(current_dir , 'analysis' , 'result.txt')

with open(result_path, "w") as file:

# add "enter" after printing each line in file and print to terminal
    for line in analysis:    
        file.write(line + "\n")
        print(line)