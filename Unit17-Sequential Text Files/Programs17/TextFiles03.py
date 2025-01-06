# TextFiles03.py
# This program demonstrates a way to check 
# if a file <exists> and also a way to see
# how many bytes a file contains.


import os 


print()
if os.path.exists("TextFiles01.txt"):
   print("TextFiles01.txt stores",
         os.path.getsize("TextFiles01.txt"),
         "bytes of data.")  
else:
   print("TextFiles01.txt does not exist.")

print()
if os.path.exists("qwerty.txt"):
   print("qwerty.txt stores",
         os.path.getsize("qwerty.txt"),
         "bytes of data.")
else:
   print("qwerty.txt does not exist.")   
