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
    
    # create variables
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
        #If new unique candidate, append the vote count(1) to the Unique_Count list 
        unique_count.append(1)
        #If an existing candidate, then do the following
      else:
        #Determine the position of the candidate in the Unique_List
        Pos=unique_list.index(Candidates)
        #Increment the value in that posistion by 1
        New_Value = unique_count[Pos] + 1
        unique_count[Pos] = New_Value   
   #Print election results and total votes 
    print("Election Results")
    print("--------------------------------------")
    print(f"Total Votes: {count}")
    print("---------------------------")
    Candidate_List_Length = len(unique_list)
    #Reset and re-use variable to now print each unique candidates vote statistics 
    Pos = 0
    #Create variables to detemrine the winner
    Winner = 0 
    Winner_Count = 0
    #Set up a lop to calculate the results and determine a winner
    for Pos in range(0, Candidate_List_Length):
      Candidate = unique_list[Pos]
      Vote_Count=unique_count[Pos]
      Candidate_Pct = Vote_Count / count*100
      #Print the results 
      print(f"{Candidate}: {Candidate_Pct}% ({Vote_Count})")
      #Calutate and determine the winner, print the winner 
      if Vote_Count > Winner_Count:
        Winner = Candidate
        Winner_Count = Vote_Count
      Pos += 1
    print(f"Winner: {Winner}")

#Set export path 
export_txt = os.path.join("analysis.txt", "report.txt")
    #create and open a new .txt file in write mode
with open(export_txt, "w") as txtfile:
    #input all results in the same style
    #remember to add "\n" for new line
    txtfile.write("Election Results " "\n")
    txtfile.write("---------------------------" "\n")
    txtfile.write(f"Total Votes: {count}" "\n")
    txtfile.write(f"--------------------------" "\n")
    txtfile.write(f"{Candidate}: {Candidate_Pct}% ({Vote_Count})", sep = "\n")
    txtfile.write(f"Winner: {Winner}""\n")
    
    
    




