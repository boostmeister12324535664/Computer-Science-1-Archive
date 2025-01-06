# TextFiles23.py
# This program will ask the user to enter 
# the name of a text file, and then use that
# text file to display a graphics background.
# Students are provided with 5 example files:
# blank.txt, Expo.txt, DK1.txt, DK2.txt, and
# DK3.txt -- the latter 3 resemble stages from
# Nintendo's Donkey Kong arcade game.
# NOTE: This same program is used for Lab 16B.


from Graphics import *;


def convert(q):
   return q * 20


def drawSpace(r,c):
   x = convert(c)
   y = convert(r)
   setColor("black")
   fillRect(x,y,20,20)


def drawGirder(r,c):
   x = convert(c)
   y = convert(r)
   setColor("red");
   fillRect(x,y,20,20)
   setColor("black")
   fillCircle(x+10,y+9,6)
   
   
def drawLadder(r,c):
   x = convert(c)
   y = convert(r)
   setColor("black")
   fillRect(x,y,20,20)
   setColor("white")
   fillRect(x,y,3,20)
   fillRect(x+16,y,4,20)
   fillRect(x,y+8,20,4)


def drawHammer(r,c):
   x = convert(c)
   y = convert(r)
   setColor("black")
   fillRect(x,y,20,20)
   setColor(150,100,15)
   fillRect(x,y,20,10)
   setColor("yellow");
   fillRect(x+8,y+10,4,10)


def drawBarrel(r,c):
   x = convert(c)
   y = convert(r)
   setColor("black")
   fillRect(x,y,20,20)
   setColor(150,100,15)
   fillRect(x+5,y,10,20)
   fillArc(x+5,y+10,5,10,180,360)
   fillArc(x+15,y+10,5,10,0,180)
   setColor("black")
   drawLine(x+16,y+9,x+16,y+13)
   drawLine(x+15,y+6,x+15,y+16)
   setColor("white")
   drawLine(x+5,y+4,x+5,y+14)
   drawLine(x+4,y+7,x+4,y+10)
   setColor(211,211,211)
   drawLine(x+5,y,x+15,y)


def drawLock(r,c):
   x = convert(c)
   y = convert(r)
   setColor("cyan")
   fillRect(x,y,20,5)
   setColor("yellow")
   fillRect(x,y+5,20,15)  


def drawPole(r,c):
   x = convert(c)
   y = convert(r)
   setColor("black")
   fillRect(x,y,20,20)
   setColor("cyan")
   fillRect(x+7,y,6,20)


def drawUnknown(r,c):  
   x = convert(c)
   y = convert(r)
   setColor("pink")
   fillRect(x,y,20,20)
   setColor("black")
   drawString("?",x+3,y+25,"Courier",16,"bold")



##########
#  MAIN  #
##########

numRows = 35
numCols = 65
fileName = textinput("Graphics Background","Enter the name of the text file.")
file = open(fileName,"r")
background = file.readlines()
file.close()

beginGrfx(1300,700)

for r in range(numRows):
   for c in range(numCols):
      if background[r][c] == '.':
         drawSpace(r,c)
      elif background[r][c] == '=':
         drawGirder(r,c)     
      elif background[r][c] == '#':
         drawLadder(r,c)     
      elif background[r][c] == 'H':
         drawHammer(r,c)     
      elif background[r][c] == 'B':
         drawBarrel(r,c) 
      elif background[r][c] == '*':
         drawLock(r,c)     
      elif background[r][c] == '|':
         drawPole(r,c)    
      else:
         drawUnknown(r,c)  
   update()                                   

endGrfx()
