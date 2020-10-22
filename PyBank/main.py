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
    net = 0
    P_L = 0
    Average = 0
    Change = 0
    Prior_P_L = 0
    #Sum_Change = 0
    Budget_List = 0
    Averge_Change = 0
    Date_List = 0
    Date_List = []
    Budget_List = []
    for row in csvreader:
        #print(row)
        #calculate row number
        count +=1
        #identify profit/loss location
        P_L = int(row[1])
        #identify date location
        Date = str(row[0])
        #calculate total profit/loss
        net = net + P_L
        #calculate average change
        Change = P_L-Prior_P_L
        #append lists
        Budget_List.append(Change)
        Date_List.append(Date)
        #Sum_Change = Sum_Change + Change
        #create loop
        Prior_P_L = P_L
    Average_Change = sum(Budget_List[1:])/len(Budget_List[1:]) 
   #find and caculate highest decrease change
    print(Budget_List)
    Min_Change = min(Budget_List)
    print(Min_Change)
    Min_Position = Budget_List.index(Min_Change)
    Min_Date = Date_List[Min_Position]
    #print average change
    #print total number of months 
    #print total profit/loss
    #print highest decrease
    print(Average_Change)
    print(f"count={count}")
    print(f"Net Profit Loss = {net} ")
    print(Budget_List)
    print(f"Minimum_Change = {Min_Date} {Min_Change}")

   

        
        