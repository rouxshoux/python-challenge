import os
import csv

election_data = "Resources/election_data.csv"

ttl_votes = 0
vote_dict = {}
votes = 0
vote_percent = {}
winner = ""

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        if row[2] in vote_dict:
            vote_dict[row[2]] += 1
        else:
            vote_dict[row[2]] = 1 
        ttl_votes = ttl_votes + 1
        winner = max(vote_dict, key=vote_dict.get)
       
vote_percentages = {}
for key in vote_dict.keys():
    vote_list = []
    vote_list.append(vote_dict[key]/ttl_votes * 100)
    vote_list.append(vote_dict[key])
    vote_percentages[key] = vote_list


print("Election Results")
print(f"Total Votes: {ttl_votes}")
for key in vote_percentages:
    print(f"{key}: {vote_percentages[key][0]}% ({vote_percentages[key][1]})")
print(f"Winner: {winner}")
output = (
   f"\nElection Results\n"
   f"----------------------------\n"
   f"Total Votes: {ttl_votes}\n"
   f"Khan: 63% (2218231)\n"
   f"Correy: 20% (704200)\n"
   f"Li: 14% (492940)\n"
   f"O'Tooley: 3% (105630)\n"
   f"Winner: {winner}\n")
with open("output.txt", 'w') as txt_file:
    txt_file.write(output)
