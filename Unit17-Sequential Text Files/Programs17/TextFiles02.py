# TextFiles02.py
# This program demonstrates how to <read> the text
# from the file created by the previous program.
# NOTE: If the previous program, TextFiles01.py,
# has not been executed, this program will crash.


file = open("TextFiles01.txt",'r')

text = file.readline()

print()
print(text)

file.close()
 