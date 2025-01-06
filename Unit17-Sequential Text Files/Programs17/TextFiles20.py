# TextFiles20.py
# This program demonstrates how to "append"  
# data to the end of an existing file.


file = open("original.txt",'a')

file.write("on alternate Tuesdays\n")
file.write("when it does not rain.\n")

file.close()
