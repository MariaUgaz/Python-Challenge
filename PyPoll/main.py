import os
import csv
candidates=[]
numv=0
votes_counter=[] 
election_data=['1','2']
csvpath = os.path.join("..","Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    
    row = next(csvReader,None)

    # votes counter
    for row in csvReader:
        numv = numv + 1
        candidate = row[2]
    if candidate in candidates:
                candidatein = candidates.index(candidate)
                votes_counter[candidatein] = votes_counter[candidatein] + 1
           
    else:
        candidates.append(candidate)
        votes_counter.append(1)
    
percentages = []
maxv = votes_counter[0]
maxi = 0

    #Percentage and winner
for count in range(len(candidates)):
        vote_perc = votes_counter[count]/numv*100
        percentages.append(vote_perc)
if votes_counter[count] > maxv:
            maxv = votes_counter[count]
            print(maxv)
            maxi = count
win = candidates[maxi]
print("Election Results")
print("--------------------------")
print(f"Total Votes: {numv}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({votes_counter[count]})")
print("---------------------------")
print(f"Winner: {win}")
print("---------------------------")
output_path = os.path.join("..", "Resources","results.csv")
with open(output_path, 'w', newline='') as csvfile:
    
    filew = filew.writer(csvfile, delimiter=',')
    
    filew.write("Election Results\n")
    filew.write("--------------------------\n")
    filew.write(f"Total Votes: {numv}\n")
for count in range(len(candidates)):
    filew.write(f"{candidates[count]}: {percentages[count]}% ({votes_counter[count]})\n")
    filew.write("---------------------------\n")
    filew.write(f"Winner: {win}\n")
    filew.write("---------------------------\n")

filew.close()