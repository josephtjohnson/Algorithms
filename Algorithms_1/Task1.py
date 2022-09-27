"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

#initialize set for containing the different numbers in the records
num_set = set()
count = 0

for t_row in texts: #iterater through texts.csv and add texter and receiver number if it is not in the set
    num_set.add(t_row[0])
    num_set.add(t_row[1])
for c_row in calls: #iterater through calls.csv and add caller or receiver number if it is not in the set
    num_set.add(c_row[0])
    num_set.add(c_row[1])

print("There are", len(num_set), "different telephone numbers in the records.")

