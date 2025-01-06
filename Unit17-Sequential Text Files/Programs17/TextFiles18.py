# TextFiles18.py
# This program demonstrates how to read information 
# from a file containing different data types.
# In this case, the "employees.txt" file contains the
# names (string values) and hourly rates (real# values)
# for several employees.  
# The file information is read into 2 "parallel arrays".  
# After that, the information in both arrays is displayed,
# and the average hourly rate is computed and displayed.


file = open("employees.txt",'r')     
names = []
hourlyRates = []      
count = 0
for lineOfText in file:
   if (count % 2 == 0):
      names.append(lineOfText.strip())
   else:
      hourlyRates.append(float(lineOfText))
   count += 1
file.close()   

count = 0
total = 0
for k in range(len(names)):
   print()
   print("Employee Name: ",names[k])
   print("Hourly Rate:   ","${:.2f}".format(hourlyRates[k]))
   total += hourlyRates[k]
   count += 1
   
average = total / count   

print("\n")
print("Average Hourly Rate:","${:.2f}".format(average))
