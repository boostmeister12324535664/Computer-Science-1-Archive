# Lab08Bst.py
# "Repetition With Traditional Graphics"
# This is the student, starting version of Lab 08B.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("Gabriel Nguyen","8B")

# Draw Grid
drawLine(325,50,325,700)
drawLine(650,50,650,700)
drawLine(975,50,975,700)
drawLine(1300,50,1300,700)
drawLine(0,375,1300,375)
drawLine(0,700,1300,700)

# Draw Red Horizontal Lines
setColor("red")
x1 = 0
y1 = 55
x2 = 325
y2 = 55
for k in range(32):
   drawLine(x1,y1,x2,y2)
   y1 += 10
   y2 += 10
   

# Draw Blue Vertical Lines

color("blue1")

for i in range(32): drawLine(i*10,375,i*10,700)
 



# Draw Magenta Diagonal Dots

color("magenta")
for i in range(32):
   drawPoint(345+((i-1)*10),680-((i-1)*10))
 
 
 
 

# Draw Green Concentric Circles

color("lightgreen")
for i in range(15):
   drawCircle(813,535,i*11)



# Draw Purple Concentric Ovals

color("violet")
for i in range(11):
   drawOval(1138,535,i*10,i*15)



# Draw Brown Concentric Squares

color("chocolate4")
for i in range(15):
   drawRegularPolygon(1138,210,i*15,4)




   
# Draw Black Concentric Regular Polygons

color("black")
for i in range(9):
   drawRegularPolygon(813,210,i*20,i+2)




# Draw Gold Sphere

color("gold")
h,v = 150,10
for i in range(14):
   drawOval(488,210,h,v)
   v += 10
h = 10
for i in range(14):
   drawOval(488,210,h,v)
   h += 10


endGrfx()
