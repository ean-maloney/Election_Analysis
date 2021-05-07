#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

import csv
import os

#Create file path variable
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a file path variable
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Create counter var
total_votes = 0

#Create candidate list
candidate_options = []

#Create candidate:votes dictionary
candidate_votes = {}

#Winning candidate variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read file.
with open(file_to_load) as election_data:

    #To do: read and analyze data.
    #Read file obj with reader func.
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
   
    for row in file_reader:
        #Increment vote total
        total_votes+=1

        #List unique candidate names
        candidate_name = row[2]

        if (candidate_name not in candidate_options):
           #Append unique candidate names to list
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

#Calculate popular vote percentages
for candidate_name in candidate_options:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    #Print names and vote info to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #Determine winner information
    if((votes > winning_count) and (vote_percentage > winning_percentage)):
        #Set winner information to highest checked info
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

    
    
        
    

#print(total_votes)
#print(candidate_options)
#print(candidate_votes)