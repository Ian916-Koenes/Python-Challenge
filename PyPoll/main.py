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
    unique_count = []
    Vote_Count = 0
    New_Value = 0
    Candidate = 0
    
    for row in csvreader:
      count += 1  
      # check if exists in unique_list or not 
      Candidates = str(row[2])
      if Candidates not in unique_list: 
        unique_list.append(Candidates)
        #
        unique_count.append(1)
        #
      else:
        #
        Pos=unique_list.index(Candidates)
        New_Value = unique_count[Pos] + 1
        unique_count[Pos] = New_Value
        #
        #unique_count(Pos) += 1     
    print("Election Results")
    print("--------------------------------------")
    print(f"Total Votes: {count}")
    print("---------------------------")
    Candidate_List_Length = len(unique_list)
    print(Candidate_List_Length)
    #
    Pos = 0
    #
    for Pos in range(0, Candidate_List_Length):
      #
      Candidate = unique_list[Pos]
      #
      Vote_Count=unique_count[Pos]
      #
      Candidate_Pct = Vote_Count / count*100
      #
      print(f"{Candidate}: {Candidate_Pct}% ({Vote_Count})")
      #
      Pos += 1
    
    #for x in str(unique_list):
      #Candidate = unique_list.append(Candidate_List_Pos)
    #for row in csvreader:
        #if Candidates == Candidate:
           #Candidate_Count += 1
    #print(f"Candidate_Count = {Candidate_Count}")
   # Candidate_Pct = Candidate_Count / count *100
    #print(f"{Candidate}: {Candidate_Pct}% ({Candidate_Count})")
    #Candidate_list_Pos =+ 1    
    
    #print(f"unique_list={unique_list}")
    #print(*unique_list, sep = "\n")
    #print(unique_list[0])
    #print(unique_list[1])
    #print(unique_list[2])
    #print(unique_list[3])




