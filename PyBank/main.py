import os
import csv

#open csv and skip header info

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

#list rows??

#create calculation variables

month_count = 0
rev_total = 0
rev_total_change = 0
#greatest_increase = ???
#greatest_decrease = ???
previous_rev = 0
month_change = []
rev_change = []


#loop through rows
#get data from first row
# go through each row
#increase month count
#add to profit/loss sum for total
#calculate change in profit/loss (between months?) + find average
#determine greatest increase
#determine greatest decrease

    for row in csvreader:
        if row[0]:
            month_count += 1
    
        if row[1]:
            def accumulate (iterable, func=row[1].add, *, initial=None):
                it = iter(iterable)
                total = initial
                if initial is None:
                    try:
                        total = next(it)
                    except StopIteration:
                        return
                yield total
                for element in it:
                    total = func(total, element)
                    yield total 
        
    #print analysis results
            
    print("Financial Analysis")
    print("______________________________________")
    print("Total Months: " + str(month_count))
    print("Total: ")
    print("Average Change: ")
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")

    #output to terminal
    #output to file