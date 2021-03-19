import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#open csv and store/skip header info
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    #create calculation variables


    #loop through rows
    for row in csvreader:

        #loop through voter ID & increase vote count
        if row[0]:
            

        #loop through candidates 
        if row[2]:

        #list candidates (unique values?)
        #count votes each candidate received
        #percent vote each candidat received
            #candidate vote count / total vote count * 100
        #winner of election based on pop.vote (largest number)
            if rev_change > increase_value:

                increase_month = row[0]
                increase_value = rev_change

    #print analysis results
    analysis = (
        f"Election Results\n"
        f"______________________________________\n"
        f"Total Votes: {month_count}\n"
        f"______________________________________\n"
        f"Khan: {rev_total:,.2f}\n"
        f"Correy: {avg_change:,.2f}\n"
        f"Li: {increase_month}\n"
        f"O'Tooley: {decrease_month}\n"
        f"______________________________________\n"
        f"Winner: "
        f"______________________________________\n")
    print(analysis)

    #output to file
    output_path = os.path.join("Analysis","PyPoll_analysis.txt")
    with open(output_path, "w") as txtfile:
        
        txtfile.write(analysis)
