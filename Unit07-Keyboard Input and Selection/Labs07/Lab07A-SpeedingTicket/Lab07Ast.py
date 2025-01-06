# Lab07Ast.pv
# "The Speeding Ticket Program"
# This is the student, starting version of Lab 07A.

print()
print("********************************************")
print("Lab 07A, The Speeding Ticket Program")
print("100 Point Version")
print("By: GABRIEL NGUYEN") # Substitute your own name here.
print("********************************************")
print("\n")


def check(v,number,fc):
   global a
   if number:
      if v.isdigit():
         a = (eval(v))
      else:
         print("\n    Error: Please enter a valid number\n\n")
         fc()
   else:
      if v == "Y" or v == "N":
        a = v
      else:
         print('\n    Error: Please enter "Y" or "N"' )
         fc()
   return a

def one():
   sL = input("What is the posted speed limit?  -->  ")
   sL = check(sL,True,one)
   return sL

def two():
   cS = (input("\nHow fast was the car travelling in mph?  -->  "))
   cS = check(cS,True,two)
   return cS

def three():
   sZ = (input("\nDid the violation occur in a school zone?  {Y/N}  -->  "))
   sZ = check(sZ,False,three)
   return sZ


sL = one()
cS = two()
sZ = three()

if cS > sL:
   t = 111+7*(cS-sL)
   if cS-sL > 30:
      t += 250
   if sZ == "Y":
      t *= 2
else:
   t = 0

print("\nTicket amount:  $",t)