# TextFiles13.py
# This program attempts to create a file of 10 random
# integers.  The program has a syntax error because 
# only string values can be written to a text file.


from random import *

seed(1234)

file = open("TextFiles13.txt",'w')

for k in range(10):
   number = randint(1000,9999)
   file.write(number)

file.close()
 