# TextFiles06.py
# This program tries to read the file created 
# by the previous program.  The problem is only 
# one <readline> command is executed, so only 
# one line of text is read and displayed.
# NOTE: If the previous program, TextFiles05.py,
#       has not been executed, this program, and
#       the next several programs, will crash.


file = open("TextFiles05.txt",'r')

lineOfText = file.readline()

print()
print(lineOfText)

file.close()
