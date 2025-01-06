# TextFiles14.py
# This program fixes the issue of the previous program
# by using the <str> command to convert the numbers to 
# strings.  However, a new issue is created; which can 
# be seen by loading the file "TextFiles14.txt".


from random import *

seed(1234)

file = open("TextFiles14.txt",'w')

for k in range(10):
   number = randint(1000,9999)
   file.write(str(number))

file.close()
 