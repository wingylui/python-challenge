import csv
path = "/Users/winglui/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv" 

# creating empty list
date = []
profitloss = []

# creating dataframe using with open and for loop, 
with open (path) as file:
    # Reading csv file using csv reader and save the header using next()
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    # for loop to convert the list from row to column 
    for row in csvreader:
        date.append(row[0])
        profitloss.append(float(row[1]))

# Creating a new column (change) for calculating the changes between months and putting a zero in the first column
# for loop: range(starting at 2 line, the length of the whole column)
# c3 = row #n - row #n-1(the previous row)
Change = []
for n in range(0, len(profitloss)):
    if n == 0:
        c3 = None
    else:
        c3 = profitloss[n] - profitloss[n-1]
    Change.append(c3)

# Creat the txt file for results
with open("./analysis/PyBank_result.txt", "w") as result:
    result.write("Financial Analysis\n")
    result.write("-----------------------------\n")
    # print the number of months using len()
    result.write(f"Total Months: {len(date)}\n")
    # print sum of the column "profit/losses" and chage int to str oformat to print result
    result.write(f"Total: ${int(sum(profitloss))}\n")
    # average of the change column
    average = sum(Change[1:])/len(Change[1:])
    result.write(f"Average Change: ${average:.2f}\n")
    # Greatest Increase in Profits (largest value in change column)
    # using .index() to identify the location of max change in the list and use it in date column
    mx = int(max(Change[1:]))
    mx_row = Change.index(mx)
    result.write(f"Greatest Increase in Profits: {date[mx_row]} (${mx})\n")
    # Greatest Decrease in Profits (smallest value in change column)
    # using .index() to identify the location of min change in the list and use it in date column
    mn = int(min(Change[1:]))
    mn_row = Change.index(mn)
    result.write(f"Greatest Decrease in Profits: {date[mn_row]} (${mn})")
result.close()