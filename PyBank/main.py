import os
import csv
months = 0
sum_rev = 0
csvpath = os.path.join("..","Resources", "budget_data.csv")
with open(csvpath,newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    line = next(csvReader,None)
    maxm = line[0]
minm = line[0]
min_rev = rev
max_rev = rev
prev_rev = rev
months = 1
sum_rev = (line[1])
sum_revch = 0
for line in csvRecsvr:
    months = months + 1
    rev=float(line[1])
    sum_rev = sum_rev + rev
    rev_change = rev - prev_rev
    sum_revch = sum_revch + rev_change
    
if rev_change > max_rev:
    maxm = line[0]
    max_rev = rev_change

if rev_change < min_rev:
    minm = line[0]
    min_rev =rev_change
prev_rev = rev
arev = sum_rev/months
avrev_change = sum_revch/(months-1)
        
print(f"Financial Analysis:")
print("-------------------------------------------------------")
print(f"Total Months: {months}")
print(f"Total Revenue: {sum_rev} USD")
print(f"Average Revenue Change: {avrev_change} USD")
print(f"Greatest Increase in Revenue: {maxm} {max_rev} USD")
print(f"Greatest Decrease in Revenue: {minm} {min_rev} USD")
print("")
save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {months}" + "\n")
    text.write(f"Total Revenue: ${sum_rev}" + "\n")
    text.write(f"Average Revenue Change: ${avrev_change}" + "\n")
    text.write(f"Greatest Increase in Revenue: {maxm} {max_rev} USD")
    text.write(f"Greatest Decrease in Revenue: {minm} {min_rev} USD")