# TextFiles12.py
# This program allows the user to enter a file name.
# Then it displays the contents of that file, 
# provided it exists.


import os 


print()
fileName = input("Enter the name of a file.  -->  ")
print()

if os.path.exists(fileName):
   file = open(fileName,'r')
   for text in file:
      text = text.strip()
      print(text)
   file.close()
else:
   print(fileName,"does not exist.")   
