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

    #loop through rows
    for row in csvreader:
        
        #increase vote count
        vote_count += 1

        #record candidate names
        name = row[2]

        #add candidates to candidate list + count votes
        if name in candidates:
            name_index = candidates.index(name)
            candidate_votes[name_index] = candidate_votes[name_index] + 1
            
        else:
            candidates.append(name)
            candidate_votes.append(1)

        print(f"{candidates} + {candidate_votes})
    #if row[0]:

            



        #list candidates (unique values?)
        #count votes each candidate received
        #percent vote each candidat received
            #candidate vote count / vote_count * 100
        #winner of election based on pop.vote (largest number)
            #if rev_change > increase_value:

                #increase_month = row[0]
                #increase_value = rev_change

    #print analysis results
    analysis = (
        f"Election Results\n"
        f"______________________________________\n"
        f"Total Votes: {vote_count}\n"
        f"______________________________________\n"
        #f"Khan: {rev_total:,.2f}\n"
        #f"Correy: {avg_change:,.2f}\n"
        #f"Li: {increase_month}\n"
        #f"O'Tooley: {decrease_month}\n"
        f"______________________________________\n"
        f"Winner: "
        f"______________________________________\n")
    print(analysis)

    #output to file
    output_path = os.path.join("Analysis","PyPoll_analysis.txt")
    with open(output_path, "w") as txtfile:
        
        txtfile.write(analysis)
