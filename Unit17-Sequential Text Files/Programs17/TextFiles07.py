# TextFiles07.py
# This program uses a <for> loop to read 
# all 5 lines of text from the file.  
# There are a couple problems.  First, there 
# are extra lines skipped in the output, caused
# by the <\n> characters used to write the
# data when the file was created.
# Second, this program only works because we
# know, ahead of time, how many lines of text
# are in the file, which is not realistic.


file = open("TextFiles05.txt",'r')

print()

for k in range(5):
   lineOfText = file.readline()
   print(lineOfText)

file.close()
