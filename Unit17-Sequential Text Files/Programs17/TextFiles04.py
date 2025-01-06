# TextFiles04.py
# This program attempts to send multiple lines
# of output to a text file.  After you run this
# program, load the file TextFiles04.txt and
# you will see this did not work properly.


file = open("TextFiles04.txt",'w')

file.write("Hello")
file.write("all")
file.write("you")
file.write("happy")
file.write("people.")

file.close()
