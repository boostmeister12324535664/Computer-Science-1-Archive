# TextFiles10.py
# This program fixes the second issue from  
# program TextFiles07.py by using the same
# <for..each> loop that works with arrays.


file = open("TextFiles05.txt",'r')

print()

for lineOfText in file:
   lineOfText = lineOfText.strip()
   print(lineOfText)

file.close()
