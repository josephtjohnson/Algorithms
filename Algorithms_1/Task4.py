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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

#initialize number list for checking against calls.csv area codes
num_set = set()

#iterate through rows in calls.csv and find specific area codes
for row in calls:
    if row[0][0:3] == '140': num_set.add(row[0])

print("These numbers could be telemarketers: " + "\n" + "\n".join(str(num) for num in sorted(num_set)))

