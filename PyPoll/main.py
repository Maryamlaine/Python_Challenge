#Library
import os
import csv
import collections as ct
from collections import Counter

# Lists to store data
row_count = 0
input = [ ]
votes = {}

# Path to collect data
election_csv = os.path.join ('Resources','election_data.csv')

# Open the csv 
with open (election_csv, newline="") as csvfile:
    reader = csv.reader (csvfile, delimiter = ",")
 
 # Read the header row first
    votes = ct.Counter()
    print(votes)
    header = next(reader)
    for row in reader:
        row_count += 1
    # Count the total number of votes each candidate won
        if row[2] not in input:
            input.append(row[2])
            votes[str(row[2])]=[1]
        else:
            votes[str(row[2])][0]+=1

#Sort the winner of the election based on popular vote
    num_of_votes=0
    for key in votes.keys():
        if int(votes[key][0]) > num_of_votes:
            num_of_votes=int(votes[key][0])
            winner_name=key

    #Count the percentage of votes each candidate won
    total_vote=sum([i[0] for i in votes.values()])
    for name in input:
        if name in votes:
            percentage_of_vote='{:.3%}'.format(float(votes[str(name)][0]/total_vote))
            votes[str(name)].append(percentage_of_vote)

    #print info and write to a new text file
    with open("PyPoll_result.txt","w") as output_file:
        #first two lines
        title='Election Results \n'+"-"*30+"\n"+"Total Votes: "+str(total_vote)+"\n"+"-"*30+"\n"
        print(title)
        output_file.write(title)
        for name in input:
            #candidate info
            candidate_info=name+": "+str(votes[str(name)][1])+" ("+str(votes[str(name)][0])+")"+"\n"
            print(candidate_info)
            output_file.write(candidate_info)
        #winner info
        Winner="-"*30+"\n"+"Winner: "+winner_name+"\n"+"-"*30
        print(Winner)
        output_file.write(Winner)



