import os 
import csv
import collections as coll

poll_data = os.path.join('Resources','Election_Data.csv')

vote_count = []
candidate_count = [] 
candidate = []

with open(poll_data) as csvfile:
    csvread = csv.reader(csvfile,delimiter=',')
    header = next(csvread)

    for rows in csvread:
        vote_count.append(rows[0])
        candidate_count.append(rows[2])

    votes_p_cand = coll.Counter(candidate_count)

print(f'E l e c t i o n   R e s u l t s')
print(f'----------------------------------')
print(f'Total votes: {"{:,.0f}".format(len(vote_count))}')
print(f'----------------------------------')
for key in votes_p_cand:
    print(f'{key}: {round((votes_p_cand[key]/len(vote_count))*100,2)}% ({"{:,.0f}".format(votes_p_cand[key])})')
print(f'----------------------------------')
print(f'Winner: {max(votes_p_cand,key=votes_p_cand.get)}')
