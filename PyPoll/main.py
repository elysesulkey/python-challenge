import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#open csv and store/skip header info
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    #create calculation variables
    vote_count = 0
    candidates = []
    candidate_votes = []
    percent_list = []

    #loop through rows
    for row in csvreader:
        
        #increase vote count
        vote_count += 1

        #record candidate names
        name = row[2]

        #add candidates to candidate list + count votes
        if name in candidates:
            name = candidates.index(name)
            candidate_votes[name] = candidate_votes[name] + 1
            
        else:
            candidates.append(name)
            candidate_votes.append(1)

    #find candidate percentage of votes
    for count in range(len(candidates)):

        candidate_percent = candidate_votes[count]/vote_count
        percent_list.append(candidate_percent)

        #winner of election based on pop.vote (largest number)
      

#print analysis results

print(f"Election Results\n")
print(f"________________________\n")
print(f"Total Votes: {vote_count}\n")
print(f"______________________________________\n")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percent_list[count]:.2%} ({candidate_votes[count]})")
print(f"______________________________________\n")
print(f"Winner: ")
print(f"______________________________________\n")
#print(analysis)

#output to file
#output_path = os.path.join("Analysis","PyPoll_analysis.txt")
#with open(output_path, "w") as txtfile:
        
    #txtfile.write(analysis)
