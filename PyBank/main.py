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
    Budget_List = 0
    Averge_Change = 0
    Date_List = 0
    Date_List = []
    Budget_List = []
    for row in csvreader:
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
        #create loop
        Prior_P_L = P_L
        #Calculate the average change
    Average_Change = sum(Budget_List[1:])/len(Budget_List[1:]) 
   #find and caculate highest decrease change
    Min_Change = min(Budget_List)
    Max_Change = max(Budget_List)
    Min_Position = Budget_List.index(Min_Change)
    Max_Position = Budget_List.index(Max_Change)
    Min_Date = Date_List[Min_Position]
    Max_Date = Date_List[Max_Position]
    #print average change
    #print total number of months 
    #print total profit/loss
    #print highest decrease and date
    #print highest increase and date
    print(Average_Change)
    print(f"count={count}")
    print(f"Net Profit Loss = {net} ")
    print(f"Minimum_Change = {Min_Date} {Min_Change}")
    print(f"Maximum_Change = {Max_Date} {Max_Change}")

   

        
        