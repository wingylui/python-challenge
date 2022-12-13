location = "/Users/winglui/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv" 

# creating empty list
date = []
profitloss = []

# creating dataframe using with open and for loop, 
with open (location) as file:
    # Reading each row (read as str format) and will show as "date,profit/losses\n"
    # (1) the \n need to be moved first using .strip(); 
    # (2) seprate date and profit/losses into a list format using .split()
    row = file.readlines()
    # Saving headers (first row) using the same method
    header = row[0].strip().split(",")
    # loop from the second row to the last
    # using column.append("values") to put the particular values into the column with the right order
    for n in row[1:]:
        c1, c2 = n.strip().split(",")
        date.append(c1)
        profitloss.append(float(c2))

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