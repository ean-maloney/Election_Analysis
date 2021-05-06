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

#Open election results and read file.
with open(file_to_load) as election_data:

    #To do: read and analyze data.
    #Read file obj with reader func.
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    #print(headers)
    #Print each row of csv file
    for row in file_reader:
       print(row)