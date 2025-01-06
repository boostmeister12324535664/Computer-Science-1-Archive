# TextFiles08.py
# This program fixes the first issue of the 
# previous program by using the <strip> command
# to "strip" away any invisible characters 
# before and after each line of text.  
# This includes </n> characters.


file = open("TextFiles05.txt",'r')

print()

for k in range(5):
   lineOfText = file.readline().strip()
   print(lineOfText)

file.close()
