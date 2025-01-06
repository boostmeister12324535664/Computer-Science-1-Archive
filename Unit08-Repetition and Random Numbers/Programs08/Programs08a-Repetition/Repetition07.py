# Repetition07.py
# This program demonstrates how to change the "step"
# value in the <for> loop.  By default, it is 1.
# To count by a number other than 1 requires adding
# a third number to the <range> command.  
# NOTE: As before, you may need to add 1 to the
# "stopping value" to make the loop work properly.


print()

for k in range(10,30,2): # Displays evens from 10 to 28
   print(k, end = " ")
   
print("\n")

for k in range(10,31,2): # Displays evens from 10 to 30
   print(k, end = " ")
   
print()
