#Election data

#import dependies
import os
import csv


#Path to collect data inside the Resource folder
d1 = os.path.join('election_data.csv')
d1_out = os.path.join('election_data.txt')

#write it to a CSV file 
with open(d1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)

# create new variables and starting values for key variables
    total_votes = 0
    candidates = []
    votes = []

#* Loop through the candidates and calculate estimates

    for row in csvreader:
        total_votes += 1 # same as total_votes = total_votes + 1  
        if row[2] in candidates:
            votes[candidates.index(row[2])] += 1
        else:
            candidates.append(row[2])
            votes.append(1)

#write results to a text file
with open(d1_out, 'w', newline='') as txtfile:

    txtfile.write('Election Results' + '\n')
    txtfile.write('-------------------------' + '\n')
    txtfile.write('Total Votes: ' + str(total_votes) + '\n')
    txtfile.write('-------------------------' + '\n')

    for y in range(len(candidates)):

        txtfile.write(candidates[y] + ': ' + str(format(votes[y] / total_votes * 100, '.3f')) + '% (' + str(votes[y]) + ')\n')

    txtfile.write('-------------------------' + '\n')
    txtfile.write('Winner: ' + candidates[votes.index(max(votes))] + '\n')
    txtfile.write('-------------------------')

with open(d1_out, newline='') as f:
    for line in f:
        print(line, end = '')