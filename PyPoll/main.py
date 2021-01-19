import os 
import csv
import collections as coll

poll_data = os.path.join('Resources','Election_Data.csv')

vote_count = [] # List to count votes
candidate_count = [] # List with names of all candidates. Names repeated based on the number of votes
candidate = [] # List with unique values of the candidates' names

with open(poll_data) as csvfile:
    csvread = csv.reader(csvfile,delimiter=',')
    header = next(csvread)

    for rows in csvread:
        vote_count.append(rows[0])
        candidate_count.append(rows[2])

    votes_p_cand = coll.Counter(candidate_count)

# Creating the text file. If it already exist it will override all the data
results_txt = open('elections_result.txt','w')
# Writing into the text file
results_txt.write('E l e c t i o n   R e s u l t s\n')
results_txt.write('------------------------------------\n')
results_txt.write('Total votes: '+ str(len(vote_count))+ '\n')
results_txt.write('------------------------------------\n')
for key in votes_p_cand:
    percentage = round((votes_p_cand[key]/len(vote_count))*100,2)
    results_txt.write(str(key) + ': ' + str(percentage)+'% (' + str(int('{:,.0f}'.format(votes_p_cand[key]))) +')\n' )
results_txt.write('------------------------------------\n')
results_txt.write('Winner: ' + max(votes_p_cand,key=votes_p_cand.get))
results_txt.close()

# Printing values 
# print(f'E l e c t i o n   R e s u l t s')
# print(f'----------------------------------')
# print(f'Total votes: {"{:,.0f}".format(len(vote_count))}')
# print(f'----------------------------------')
# for key in votes_p_cand:
#     print(f'{key}: {round((votes_p_cand[key]/len(vote_count))*100,2)}% ({"{:,.0f}".format(votes_p_cand[key])})')
# print(f'----------------------------------')
# print(f'Winner: {max(votes_p_cand,key=votes_p_cand.get)}')
