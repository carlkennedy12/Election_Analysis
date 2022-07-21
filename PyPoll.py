import os
import csv

file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_load = os.path.join("Resources", "election_results.csv")
#open file to variable named 'election_data' and 'election_analysis'
outfile = open(file_to_save, "w")
election_data = open(file_to_load)

#analysis of data below

#establish vote counter and candidate options and candidate votes
candidate_options = []
total_votes = 0
candidate_votes = {}
#read csv file
file_reader = csv.reader(election_data)

#read header row
headers = next(file_reader)

#count votes and add to total votes counter
for row in file_reader:
    total_votes +=1
    
    #print candidate name from each row
    candidate_name = row[2]
    if candidate_name not in candidate_options:
        
        
        candidate_options.append(candidate_name)

        candidate_votes[candidate_name] = 0

    candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    #print vote count to terminal

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
     
     #save to txt file

    txt_file.write(election_results) 

    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]
        
        vote_percentage = float(votes) / float(total_votes) * 100
        
        

    #Winning Candidate and Winning Count Tracker
        winning_candidate = ''
        winning_count = 0
        winning_percentage = 0
    #print each 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
        
            winning_percentage = vote_percentage
            
            winning_candidate = candidate_name
        
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #output(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)








    #close file
    election_data.close()
    outfile.close()