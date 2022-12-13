location = "/Users/winglui/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv" 

id = []
country = []
candidate = []

# creating dataframe using with open and for loop (list format), 
with open (location) as file:
    # Reading each row (read as str format) and will show as "Ballot ID, Country, Candidate"
    # (1) the \n need to be moved first using .strip(); 
    # (2) seprate date and profit/losses into a list format using .split()
    row = file.readlines()
    # Saving headers (first row) using the same method
    header = row[0].strip().split(",")
    # loop from the second row to the last
    # using column.append("values") to put the particular values into the column with the right order
    for n in row[1:]:
        c1, c2, c3 = n.strip().split(",") 
        id.append(c1)
        country.append(c2)
        candidate.append(c3)

# using set() to identify the unique candidate and put them into unique candidate list
unique_can = list(set(candidate))
# number of vote counts for each individuals and put them into vote_count list (in order)
vote_count = []
for v in range(len(unique_can)):
    c5 = candidate.count(unique_can[v])
    vote_count.append(c5)


# Creat the txt file for results
with open("./analysis/election_results.txt", "w") as result:
    result.write("Election Results\n")
    result.write("--------------------------------\n")
    # using len() to count total votes
    result.write(f"Total Votes: {len(candidate)}\n")
    result.write("--------------------------------\n")
    # loop the 3 candidate and create a dictionary
    for i in range(len(unique_can)):
        result.write("{candidate_name}: {percentage}% ({votes})\n".format(
            candidate_name = str(unique_can[i]),
            percentage = f"{vote_count[i]/len(id)*100:.3f}",
            votes = f"{vote_count[i]}"
        ))
    result.write("--------------------------------\n")
    # identifying the highest number of votes using max() and then;
    # using index() to find the position in the vote_count list
    # print the winner name from unique_can list
    result.write(f"Winner: {unique_can[vote_count.index(max(vote_count))]}\n")
    result.write("--------------------------------")
result.close()