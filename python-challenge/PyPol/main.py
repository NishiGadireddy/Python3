import os
import csv
csvpath = os.path.join("election_data.csv")

def FindWinner(names, percents):
   win=float(percents[0])
   winner = names[0]
   for count in percents:
       if float(count) > win:
           winner = names[count.index()]
   return winner

count = 0
Candidates = []
CandVote = []
CandPercent = []

with open(csvpath,newline='')as csvfile:
   csvreader = csv.reader(csvfile,delimiter=',')
   header = next(csvreader, None)
   for row in csvreader:
       count +=1
       if row[2] not in Candidates:
           Candidates.append(row[2])
           CandVote.append(1)
       else:
           votefor = Candidates.index(row[2])
           CandVote[votefor] += 1
   for votes in CandVote:
       Percent = float(votes/count*100)
       CandPercent.append(Percent)
   winner = FindWinner(Candidates,CandVote)


print("Election Results")
print("----------------")
print(f"Total Votes:{count} ")
print("------------------")
for i in range(len(Candidates)):
   print(f"{Candidates[i]}: {round(CandPercent[i],2)}% ({CandVote[i]} votes)")
print("-------------------")
print(f"{winner} is the winner.")


f = open("Election.txt", "w+")
f.write("Election Results" "\n")
f.write("----------------" "\n")
f.write(f"Total Votes:{count}" "\n")
f.write("------------------" "\n")
for i in range(len(Candidates)):
   f.write(f"{Candidates[i]}: {round(CandPercent[i],2)}% ({CandVote[i]} votes)" "\n")
f.write("-------------------" "\n")
f.write(f"{winner} is the winner." "\n")
f.close
