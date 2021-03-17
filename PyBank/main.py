import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    month_count = -1

    for row in csvreader:
        month_count += 1
    
    print("Financial Analysis")
    print("______________________________________")
    print("Total Months: " + str(month_count))
    print("Total: ")
    print("Average Change: ")
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")