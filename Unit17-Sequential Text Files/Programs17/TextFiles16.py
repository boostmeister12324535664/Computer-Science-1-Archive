# TextFiles16.py
# This program attempts to read in the numbers from the
# file created by the previous program and average them.
# The problem is the numbers are stored as text and need to
# be converted back to numbers before they can be averaged.


file = open("TextFiles15.txt",'r')

print()

total = 0
count = 0

for number in file:
   print(number)
   total += number
   count += 1

file.close()

average = total / count

print()
print("Total   =",total)
print()
print("Average =",average)
