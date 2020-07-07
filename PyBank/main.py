#Library
import os
import csv
import statistics
from statistics import mean


# Set up a path to collect the data
budget_csv = os.path.join ('Resources','budget_data.csv')

# Open the csv 
with open (budget_csv, newline="") as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")

#Read the header row first
    next(csvreader)
    first_row = next(csvreader)
    prv = int(first_row[1])
    Net_loss = 0

# Total number of months included in the dataset
    Column = list(csvreader)
    row_count = len (Column)
    #print(row_count)
    
#    
    Net_total = 0
    Net_list =[]
    for i in Column:
        Net_total += int(i[1])
        Net_loss = int(i[1])- prv
        prv = int(i[1])
        Net_list.append(Net_loss)
    #print (Net_total)

#print (Net_list)
# Average of changes in profit/losses 
Average_changes = statistics.mean(Net_list) 
print(round(Average_changes, 2))
#print(Net_list)

Max_increase_profit = 0
for i in range (0,len(Net_list)):
    if Max_increase_profit < Net_list[i]:
       Max_increase_profit = Net_list[i] 
       max_index=i
print ("max:", Max_increase_profit,"index",max_index)                    
print (Column[max_index][0])

Min_decrease_loss = 0
for i in range (0,len(Net_list)):
    if Min_decrease_loss > Net_list[i]:
       Min_decrease_loss = Net_list[i] 
       min_index=i
print ("min:", Min_decrease_loss,"index",min_index)                    
print (Column[min_index][0])

#Library
import os
import csv
import statistics
from statistics import mean


# Set up a path to collect the data
budget_csv = os.path.join ('.','budget_data.csv')

# Open the csv 
with open (budget_csv, newline="") as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")

#Read the header row first
    next(csvreader)
    first_row = next(csvreader)
    prv = int(first_row[1])
    Net_loss = 0

# Total number of months included in the dataset
    Column = list(csvreader)
    row_count = len (Column)
    #print(row_count)
    
#    
    Net_total = 0
    Net_list =[]
    for i in Column:
        Net_total += int(i[1])
        Net_loss = int(i[1])- prv
        prv = int(i[1])
        Net_list.append(Net_loss)
    #print (Net_total)

#print (Net_list)
# Average of changes in profit/losses 
Average_changes = statistics.mean(Net_list) 
print(round(Average_changes, 2))
#print(Net_list)

Max_increase_profit = 0
for i in range (0,len(Net_list)):
    if Max_increase_profit < Net_list[i]:
       Max_increase_profit = Net_list[i] 
       max_index=i
print ("max:", Max_increase_profit,"index",max_index)                    
print (Column[max_index][0])

Min_decrease_loss = 0
for i in range (0,len(Net_list)):
    if Min_decrease_loss > Net_list[i]:
       Min_decrease_loss = Net_list[i] 
       min_index=i
print ("min:", Min_decrease_loss,"index",min_index)                    
print (Column[min_index][0])

# Zip lists together
Summary_table_csv = zip()
Values = [row_count, Net_total, Average_changes, Max_increase_profit, Min_decrease_loss]
Titles = ["Total Months:  ", "Net_Total: $", "Average_Change: $", "Greatest Increase in Profits: $", "Greatest Decrease in Profits: $"]
Summary_table_csv = zip(Titles, Values)

 # Set variable for output file
output_file = os.path.join("PyBank_results.txt")

#  Open the output file
pybank_file = open(output_file, "w")
for Titles, Values in Summary_table_csv:
    pybank_file.write(str(Titles))
    pybank_file.write(str(Values))
    pybank_file.write("\n")
    print(Titles, Values)




