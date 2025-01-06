# Lab08Cvst.py
# "Random Graphics"
# This is the student, starting version of Lab 08C.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("Gabriel Nguyen","8C")

# Draw Grid
drawLine(325,50,325,700)
drawLine(650,50,650,700)
drawLine(975,50,975,700)
drawLine(1300,50,1300,700)
drawLine(0,375,1300,375)
drawLine(0,700,1300,700)

def r(xx,yy):
   return randint(xx,yy)
   
def s():
   setRandomColor()

# Draw 1000 Random Points.
for k in range(1000):
   setRandomColor()
   x = randint(5,320)
   y = randint(55,370)
   drawPoint(x,y)
update()

# Draw 500 Random Lines.

for i in range(500):
   s(); drawLine(r(980,1295),r(380,695),r(980,1295),r(380,695))


# Draw 100 Random Rectangles.

for i in range(100):
   s(); fillRectangle(r(655,970),r(380,695),r(655,970),r(380,695))


# Draw 100 Random Triangles.
for i in range(100):
   s(); fillPolygon([r(330,645),r(380,695),r(330,645),r(380,695),r(330,645),r(380,695)])



# Draw Your Initials 100 Times with random sizes.

for i in range(100):
   ahh = r(10,36) #not to be confused with "aah"
   s(); drawString("GN",r(5,320-2*ahh),r(380+2*ahh,695),"Arial",ahh)



# Draw 100 Random Stars with a constant radius 
# of 50 and a random # of Points.

for i in range(100):
   s(); fillStar(r(1025,1250),r(105,320),50,r(5,10))


# Draw 100 Random Circles with random radii.

for i in range(100):
   aah = r(1,75) #not to be confused with "ahh"
   s(); fillCircle(r(655+aah,970-aah),r(55+aah,370-aah),aah)#not the best way to do this
     
  
# Draw 100 Random Arcs with random horizontal radii,
# vertical radii, starting points and stopping points.

for i in range(100):
   hey = r(1,75)
   hello = r(1,75)
   s(); fillArc(r(330+hey,645-hey),r(55+hello,370-hello),hey,hello,r(0,360),r(0,360))
   



endGrfx()
