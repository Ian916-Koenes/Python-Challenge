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

    for row in csvreader:
      count += 1
      Candidates = str(row[2])
      #Votes = int(row[0])
      # function to get unique values 
      def unique(list1): 
  
    # intilize a null list 
      unique_list = [] 
      
    # traverse for all elements 
      for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(candidates) 
    # print list 
    for x in unique_list: 
        print(Candidates)

    print(f"count={count}")




