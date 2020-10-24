#Import os module
import os
import csv

#set path for file
csvpath = os.path.join("Resources", "election_data.csv")
print(csvpath)

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")
    print(csvpath)
    csv_header=next(csvreader)

    count = 0
    Votes = 0
    Candidates = 0
    unique_list = [] 

    for row in csvreader:
      count += 1
      
      # function to get unique values 
       
  
    # intilize a null list 
      
      
    # traverse for all elements  
      # check if exists in unique_list or not 
      Candidates = str(row[2])
      if Candidates not in unique_list: 
        unique_list.append(Candidates)
             
        

    print("Election Results")
    print("--------------------------------------")
    print(f"Total Votes: {count}")
    print("---------------------------")
    
    Candidate_List_Length = len(unique_list)
    Candidate_List_Pos = 0
    Candidate_Count = 0
    Candidate_Pct = 0.00000
    Candidate = 0

    for x in str(Candidate_List_Length):
      Candidate = unique_list.append(Candidate_List_Pos)
      for row in csvreader:
            if Candidates == Candidate:
              Candidate_Count += 1
      Candidate_Pct = Candidate_Count / count *100
      print(f"{Candidate}: {Candidate_Pct}% {Candidate_Count}")
      Candidate_list_Pos =+ 1    
    
    #print(f"unique_list={unique_list}")
    #print(*unique_list, sep = "\n")
    #print(unique_list[0])
    #print(unique_list[1])
    #print(unique_list[2])
    #print(unique_list[3])




