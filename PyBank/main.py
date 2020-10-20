#Import os module 
import os
import csv

#set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

with open(csvpath) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=",")
    print(csvpath)
    csv_header=next(csvreader)

    count = 0
    for row in csvreader:
        print(row)
        count +=1

    print(f"count={count}")

    net = 0
    P_L = 0
    for row in csvreader:
       P_L = int(row, 2)
       net = net + P_L
    print(f"Net Profit Loss = {net} ")
   

        
        