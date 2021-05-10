# Election_Analysis

## Project Overview
The Colorado Board of Elections has requested an audit of a congressional election consisting of the following information:
  1. Total votes cast.
  2. Complete list of candidates receiving votes.
  3. Votes received by each candidate.
  4. Percentage of votes received by each candidate.
  5. Winner of election based on popular vote.  
  6. Voter turnout by county.
  7. Percentage of total vote from each county.
  8. County with highest turnout.
 
 ## Resources 
 - Data Source: election_results.csv
 - Software: Python 3.7.6, Visual Studio Code 1.56

(NOTE: Because Visual Studio has non-standard defaults for setting the current working directory,           I have included two sets of file paths in lines 8-16 of my code. The first set works when running the code is Visual Studio under its default settings, but the second (commented-out) set of paths may need to be activated when running the code in a different environment. Doing so merely requires that lines 10 and 11 be commented out, and lines 15 and 16 be un-commented.)

## Results
The election audit shows that the following:
  1. 369,711 votes were cast.
  2-4. Three candidates received votes: 
    i. Charles Casper Stockham received 85,213 votes (23.0%).
    ii. Diana DeGette received 272,892 votes (73.8%).
    iii. Raymon Anthony Doane received 11,601 votes (3.1%).
  5. The election winner was Diana DeGette.
  6-7. The three counties represented were:
    i. Jefferson: 38,855 votes (10.5%)
    ii. Denver: 306,055 votes (82.8%)
    iii. Arapahoe: 24,801 votes (6.7%)
  8. The county with the highest turnout was Denver County.

## Summary
The script can be easily modified for use in other election audits based on the same format of CSV-data by simply changing the file path in line 10 to the path for the relevant CSV file. 

```file_to_load = os.path.join("Resources", "election_results.csv")```

In the code, the folder containing our data (sitting in the same directory as out .py file) is called "Resources" and the file name of our data is "election_results.csv." This is the only place in the program where these names are relevant, so changing them here will allow the script to be run for a different file. For example, if we had a CSV file named "voting_data.csv," so long as that file is in the same directory as our .py file, we can modify the above code to read:

```file_to_load = os.path.join("voting_data.csv")```

and the script will run without issue.

This program can also be run for elections with differently defined regions (e.g., with voting precints or electoral districts instead of counties) without any technical changes, though it would make the most sense to at least change the output formatting to reflect the type of region used. For example, one would want to change the output variable in lines 116-119,

```
largest_county_message = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county} ({largest_county_votes:,})\n"
        f"-------------------------\n") 
```
       
such that it reads, for example, ```Largest Precint Turnout``` instead of ```Largest County Turnout```. Additionally, many of the variable names throughout the script make reference to "county" (e.g., ```largest_county_message```, ```largest_county```, etc.). These need not be altered for the program to work with different regions, but a careful editor could alter them throughout to make the code easier to understand for a human reader.
