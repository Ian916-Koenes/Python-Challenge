#Import os module 
import os
import csv

#set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")


with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csv, delimiter=",")
    print(cvsreader)
    csv_header=next(csvreader)

    for row in csvreader:
        