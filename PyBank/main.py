import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#open csv and store/skip header info
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #create calculation variables

    row = next(csvreader)
    month_count = 1
    rev = float(row[1])
    rev_total = 0
    rev_change = 0
    previous_rev = rev
    sum_change = 0
    rev_total = float(row[1])
    #greatest_increase = ???
    #greatest_decrease = ???

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

            #calculate change in profit/loss 
    
            rev_change = rev - previous_rev

            sum_change = sum_change + rev_change
            
            previous_rev = rev

            #determine greatest increase
            value = float(row[1])
          
            for value in range(int(row[1])):

                if int(row[1]) >= value:
                    greatest_increase = int(row[1])
                    print(f'greatest increase {greatest_increase}')

                #if rev_increase_1 >= rev_change:
                    #rev_increase = rev_increase_1

                increase_month = row[0]

               #compare values
                
            #determine greatest decrease
            if rev_change <= 0:
                rev_decrease = rev_change
                decrease_month = row[0]
                print(f'{row[0]} + decrease {rev_decrease}')
                #compare values

    #finish average change calculation 
    avg_change = sum_change/month_count

    #print analysis results      
    print(f"Financial Analysis")
    print(f"______________________________________")
    print(f"Total Months: {month_count} ")
    print(f"Total: ${rev_total:,.2f}")
    print(f"Average Change: ${avg_change:,.2f}")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Decrease in Profits: ")

    #output to terminal
    #output to file