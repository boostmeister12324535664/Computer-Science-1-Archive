# TextFiles09.py
# This program demonstrates what happens when you
# attempt to read past the end of a text file.
# In most languages, this would crash the program.
# In Python, you just get extra blank lines.


file = open("TextFiles05.txt",'r')

print()

for k in range(8):
   lineOfText = file.readline().strip()
   print(lineOfText)

file.close()
