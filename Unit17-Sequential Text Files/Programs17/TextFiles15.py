# TextFiles15.py
# This program fixes the issue of the previous 
# program by adding a "new line escape sequence" <\n> 
# as was done in earlier program examples.


from random import *

seed(1234)

file = open("TextFiles15.txt",'w')

for k in range(10):
   number = randint(1000,9999)
   file.write(str(number)+"\n")

file.close()
 