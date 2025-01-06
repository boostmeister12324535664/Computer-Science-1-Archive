# TextFiles11.py
# This program demonstrates the <readlines> command which
# reads in the ENTIRE file and creates an array of strings.


file = open("TextFiles05.txt",'r')
allLinesOfText = file.readlines()
file.close()

print()
for lineOfText in allLinesOfText:
   lineOfText = lineOfText.strip()
   print(lineOfText)
 