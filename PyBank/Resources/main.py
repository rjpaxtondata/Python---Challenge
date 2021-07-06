#import dependencies
import os

import csv

# for reading CSV files
csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

#stores all of the text inside a variable called lines
lines = csvfile.read()

#prints the contents of the text file
print(lines)

#total number of months (cant get this to work)

#x = len(fp.readlines())
#print('Total lines:', x)



#Net total amoung of "profit/loses" over entire period


#The average of the changes in "profit/loses" over entire period


#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (data and amount ) over the entire period