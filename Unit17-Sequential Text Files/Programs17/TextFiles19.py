# TextFiles19.py
# This program reads an original file and writes 
# a backup file with the exact same contents.
# It demonstrates that a program can read from 
# and/or write to multiple files simultaneously.
# After you run the program, load both original.txt
# and backup.txt and you should see the two files
# are identical.


inFile = open("original.txt",'r')
outFile = open("backup.txt",'w')

print()

for lineOfText in inFile:
   outFile.write(lineOfText)

inFile.close()
outFile.close()
