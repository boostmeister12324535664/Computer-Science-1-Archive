# TextFiles05.py
# This program fixes the issue of the 
# previous program by adding the 
# "new line escape sequence" <\n>.


file = open("TextFiles05.txt",'w')

file.write("Hello\n")
file.write("all\n")
file.write("you\n")
file.write("happy\n")
file.write("people.\n")

file.close()
