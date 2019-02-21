import csv
import os

file_path = os.path.join("raw_data","election_data.csv")

with open(file_path, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    csvheader = next(reader)

    candidate = []

    for row in reader:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
    
    votes = []
    name = []
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidate)

correy_total = candidate.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidate.count('Li')
li_percent = li_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

print(f'Election Results')
