"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#initialize a dictionary to make key:value pairings for phone numbers to call time 
count = 0
call_dict = dict()
for row in calls:
    if row[0] in call_dict: #if caller in dict, increment time
        call_dict[row[0]] += int(row[3])
    elif row[0] not in call_dict: #if caller not in dict, add number and time
        call_dict[row[0]] = int(row[3])
    if row[1] in call_dict: #if receiver in dict, increment time
        call_dict[row[1]] += int(row[3])
    elif row[1] not in call_dict: #if receiver not in dict, add number and time
        call_dict[row[1]] = int(row[3])


print(max(call_dict, key=call_dict.get), "spent the longest time,", max(call_dict.values()), "seconds, on the phone during September 2016.")




