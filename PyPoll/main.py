#import csv
import csv
votes =[]
with open('Resources/election_data.csv') as csvfile:
    data=csv.reader(csvfile)
    for row in data:
        if row[2]=="Candidate":
            continue
        votes.append(row[2])

print("Election Results")
print('-------------------------')
print('Total Votes: '+str(len(votes)) )
print('-------------------------')
candidates = set(votes)
winner = ""
maximum=0
for c in list(candidates):
    if votes.count(c)>maximum:
        maximum = votes.count(c)
        winner = c 
    print(f'{c}: ({"{:.3f}".format(votes.count(c)/len(votes)*100)}%) {votes.count(c)}')
print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')