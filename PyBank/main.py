# #Import os module 
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
    net = 0
    P_L = 0
    Average = 0
    Change = 0
    Prior_P_L = 0
    Sum_Change = 0
    Budget_List = 0
    Averge_Change = 0
   
    Budget_List = []
    for row in csvreader:
        print(row)
        count +=1
        P_L = int(row[1])
        net = net + P_L
        Change = P_L-Prior_P_L
        Budget_List.append(Change)
        Sum_Change = Sum_Change + Change
        Prior_P_L = P_L
    Average_Change = sum(Budget_List[1:])/len(Budget_List[1:]) 
    print(Average_Change)
    print(f"count={count}")
    print(f"Net Profit Loss = {net} ")
    print(Budget_List)

   

        
        