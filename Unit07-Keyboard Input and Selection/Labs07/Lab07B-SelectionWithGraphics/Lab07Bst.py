# Lab07Bst.py
# "Selection With Graphics"
# This is the student, starting version of Lab 07B.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("Gabriel Nguyen","7B")

def clear():
   setColor('white');fillRectangle(0,80,1300,700);setColor('black')

def check(x,a,b):
   A = ("either",a,"or",b)
   if isinstance(x,float):
         x = int(x)
         A = "a number between",a,"and",b
   if (a<=x<=b) or (x == a or x == b): #split for strings
      clear()
      return x
   else:
      drawString(('Error... Please enter',A),20, 260,"TimesRoman",30) #I am unsure of how to get rid of these commas and parenthesis without extending or breaking the code
      

def S():
   s = None
   while s == None:
      s = numinput("Shape Selection","1 = Line \n2 = Rectangle \n3 = Circle \n4 = Oval \n5 = Regular Octagon \n6 = Star \n7 = Burst")
      s = check(s,1,7)
   return s
def C():
   c = None
   while c == None:
      c = numinput("Color Selection","1 = Red\n2 = Orange\n3 = Yellow\n4 = Green\n5 = Blue\n6 = Purple\n7 = Brown")
      c = check(c,1,7)
   return c
def W(): 
   w = None 
   while w == None:
      w = numinput("Width Selection","Enter 1-100")
      w = check(w,1,100)
   return w
def F():
   f = None
   while f == None:
      f = textinput("Want the shape filled?","Enter Y for 'Yes' and N for 'No'.")
      f = check(f,"Y","N")
   return f

s = S()
c = C()
w = W()
f = F()

colors = ['red','orange','yellow','green','blue','purple','brown']
setColor(colors[c-1])

width(w)

def line():
   drawLine(100,350,1200,350)
def fRect():
   fillRectangle(200,200,1100,500)
def fCircle():
   fillCircle(650,350,250)
def fOval():
   fillOval(650,350,400,200)
def fOcto():
   fillRegularPolygon(650,350,250,8)
def fStar():
   fillStar(650,350,250,5)
def fBurst():
   fillBurst(650,350,250,21)
def Rect():
   drawRectangle(200,200,1100,500)
def Circle():
   drawCircle(650,350,250)
def Oval():
   drawOval(650,350,400,200)
def Octo():
   drawRegularPolygon(650,350,250,8)
def Star():
   drawStar(650,350,250,5)
def Burst():
   drawBurst(650,350,250,21)

fshapes = [line,fRect,fCircle,fOval,fOcto,fStar,fBurst,line,Rect,Circle,Oval,Octo,Star,Burst]

if f == "Y":
   fshapes[s-1]()
else:
   fshapes[s+6]()
endGrfx() 
  