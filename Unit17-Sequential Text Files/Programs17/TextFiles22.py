# TextFiles22.py
# This program demonstrates that data from a 
# text file can be used in a graphics program.


from Graphics import *


def drawBlueSquare(x):
   setColor("blue")
   x = x * 50 + 25
   fillRegularPolygon(x,175,30,4)


def drawRedCircle(x):
   setColor("red")
   x = x * 50 + 25
   fillCircle(x,175,25)
   
   
def drawGreenTriangle(x):
   setColor("green")
   x = x * 50 + 25
   fillRegularPolygon(x,183,27,3)   



##########
#  MAIN  #
##########

file = open("TextFiles22.txt",'r')
lineOfText = file.readline()
file.close()

beginGrfx(1300,350)

for x in range(len(lineOfText)):
   if lineOfText[x] == "S":
      drawBlueSquare(x)
   elif lineOfText[x] == "C": 
      drawRedCircle(x)
   elif lineOfText[x] == "T": 
      drawGreenTriangle(x)      

endGrfx()
