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
    #Votes = 0
    Candidates = 0
    #Vote_List = []
    #Candidate_List = []
    unique_list = [] 

    for row in csvreader:
      count += 1
      
      #Votes = int(row[0])
      # function to get unique values 
      def unique(list1): 
  
    # intilize a null list 
      
      
    # traverse for all elements 
        for Candidates in list1: 
        # check if exists in unique_list or not 
          Candidates = str(row[2])
          if x not in unique_list: 
            unique_list.append(Candidates) 
    # print list 
          for Candidates in unique_list: 
        

            print(f"count={count}")
            print(f"Candidates={Candidates}")



