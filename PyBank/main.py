import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#create calculation variables

month_count = 0
rev = 0
rev_total = 0
#rev_total_change = 0
#greatest_increase = ???
#greatest_decrease = ???
#previous_rev = 0
#month_change = []
#rev_change = []

#open csv and store/skip header info
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    #loop through rows
    for row in csvreader:

        #loop through month & increase month count
        if row[0]:
            month_count += 1

        #loop through profit/loss   
        if row[1]:

            #add to profit/loss sum for total 
            rev = float(row[1])
            rev_total = rev_total + rev

            #calculate change in profit/loss + find average
                #current month - previous month (between each month)
                #sum of changes / number of changes (86 months?)
                
            #determine greatest increase
            #determine greatest decrease

    #print analysis results
            
    print(f"Financial Analysis")
    print(f"______________________________________")
    print(f"Total Months: {month_count} ")
    print(f"Total: ${rev_total:,.2f}")
    print(f"Average Change: ")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Decrease in Profits: ")

    #output to terminal
    #output to file