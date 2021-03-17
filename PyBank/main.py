import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    month_count = 0

    profit_total = 0

    for row in csvreader:
        if row[0]:
            month_count += 1
    
        #if row[1]:
           # profit_total =
           
    print("Financial Analysis")
    print("______________________________________")
    print("Total Months: " + str(month_count))
    print("Total: ")
    print("Average Change: ")
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")