# TextFiles17.py
# This program fixes the issue of the previous 
# program by using the <int> command to convert
# the text numbers back into integer values.  
# NOTE: This process also eliminates the <\n> 
#       escape sequence character.


file = open("TextFiles15.txt",'r')
print()
total = 0
count = 0

for lineOfText in file:
   number = int(lineOfText)
   print(number)
   total += number
   count += 1

file.close()

average = total / count

print()
print("Total   =",total)
print()
print("Average =",average)
