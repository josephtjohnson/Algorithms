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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#initialize number list for checking against calls.csv area codes
number_list = ['(080)','7', '8', '9', '0','140']
num_list = list()
perc_count = 0

#iterate through rows in calls.csv and find specific area codes
for row in calls:
    if number_list[0] in row[0]: #searches for caller from a land line
        if row[1][0] in number_list[1:4]: #verifies receiver is a mobile area code
            num_list.append(row[1][0:4])
        elif row[1][0] in number_list[0][0]: #verifies if receiver is a land line area code
            code = row[1].split('(')
            code = code[1].split(')')
            num_list.append(code[0])
            if row[1][1:4] == '080': #if land line and area code (080) add to perc_count for Part B calculation
                perc_count += 1
        elif row[1][0:3] in number_list[5]: #verifies if receiver is a telemarketer, although a very unlikely situation
            num_list.append(row[1][0:3])

#create sorted set to only see unique area codes
num_set = set(num_list)
print("\nThe numbers called by people in Bangalore have codes: \n")            
for ac in sorted(num_set):
    print(ac, '\n')

#calculate percentage of calls made from land line to a land line
perc_calls = round((perc_count/len(num_list) * 100),2)
print(perc_calls, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")










        



    
#all numbers called by people of Bangalore have been added to the set. Now they need to be sorted, area codes extracted, and printed out to complete Part A.



