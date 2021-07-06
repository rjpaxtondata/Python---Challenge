#Bank Data

#import dependencies
import os
import csv

# Path to the file
d2 = os.path.join('budget_data.csv')
d2_out = os.path.join('d2output.txt')

# Set variable starting values
totalMonths = 0
totalRevenue = 0
prevRevenue = 0
averageChange = 0
revChange = 0
# store both date & the change
greatestInc = ["", 0]
greatestDec = ["", 9999999999999999999999]

revenueChanges = []

# Read Files
with open(d2, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    file_header = next(csvreader)
    # Loop through all the rows of data we collect
    for row in csvreader:

        # Calculate the totals
        totalMonths = totalMonths + 1
        totalRevenue = totalRevenue + int(row[1])
        # Keep track of changes
        if(prevRevenue != 0):
            revChange = int(row[1]) - prevRevenue
        # Reset the value of prev_revenue to the row I completed my analysis
        prevRevenue = int(row[1])

        # Determine the greatest increase
        if (revChange > greatestInc[1]):
            greatestInc[1] = revChange
            greatestInc[0] = row[0]

        # Determine the greatest decrease
        if (revChange < greatestDec[1]):
            greatestDec[1] = revChange
            greatestDec[0] = row[0]
        revenueChanges.append(revChange)

    # calculate average change from revenue change list, should be length -1 as first record is blank
    averageChange = sum(revenueChanges)/(len(revenueChanges)-1)

    # print output to terminal as follows:
    print("")
    print("--------------------------------------------------")
    print("Financial Analysis")
    print("--------------------------------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Revenue: $ {totalRevenue}")
    print(f"Average Change: {round(averageChange,2)}")
    print(f"Greatest Increase in Profits: {greatestInc[0]}, (${greatestInc[1]})")
    print(f"Greatest Decrease in Profits: {greatestDec[0]}, (${greatestDec[1]})")
    print("--------------------------------------------------")
    print("")

    # print output to the file
with open(d2_out, "w") as txtFile:
    txtFile.write("Total Months: " + str(totalMonths))
    txtFile.write("\n")
    txtFile.write("Revenue: " + "$" + str(totalRevenue))
    txtFile.write("\n")
    txtFile.write("Average Change: " + "$" + str(round(averageChange,2)))
    txtFile.write("\n")
    txtFile.write("Greatest Increase: " + str(greatestInc[0]) + ", ($" + str(greatestInc[1]) + ")") 
    txtFile.write("\n")
    txtFile.write("Greatest Decrease: " + str(greatestDec[0]) + ", ($" + str(greatestDec[1]) + ")")