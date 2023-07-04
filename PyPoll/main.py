import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')
results_file = os.path.join('analysis', 'results.txt')

total_votes = 0
candidate_counts = {}

with open(election_csv, 'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    header = next(election_data)

    for row in election_data:
        'count votes'
        total_votes += 1
        candidate = row[2]
        'if candidate already exists, add 1 vote to the candidate. Else create new candidate with 1 vote'
        if candidate in candidate_counts:
            candidate_counts[candidate] += 1
        else:
            candidate_counts[candidate] = 1

'creating strings to print to terminal and output as text file'
results = f"Election Results\n-------------------------\n"
results += f"Total Votes: {total_votes}\n"
results += f"-------------------------\n"

'get percentages and continue adding to results'
for candidate, count in candidate_counts.items():
    percentage = (count / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({count})\n"

results += f"-------------------------\n"

'check which candidate has the most votes'
winner = max(candidate_counts, key=lambda x: candidate_counts[x])
results += f"Winner: {winner}\n"
results += f"-------------------------\n"

print(results)
print("The results have been saved to:", results_file)

with open(results_file, "w") as txt_file:
    txt_file.write(results)