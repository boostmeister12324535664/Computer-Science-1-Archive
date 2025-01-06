### DRAWING PROCEDURES ###

from Graphics import *



def draw(s,c='black'):
   color(c)
   for i in range(len(s)//2-1):
      drawLine(s[i*2],s[i*2+1],s[i*2+2],s[i*2+3])

def lerpLine(x,y,xx,yy,ii,p):
   width(randint(3,5))
   setRandomColor()
   for i in range(ii):
      drawLine(x+(xx-x)*i/ii-p,y+(yy-y)*i/ii,x+(xx-x)*i/ii+p,y+(yy-y)*i/ii)

def Lp(z,a,c):
   points = []
   for i in range(len(z)//2):
      if i == len(z)//2-1:
         x1,y1,x2,y2 = z[-2],z[-1],z[0],z[1]
      else:  
         x1,y1,x2,y2 = z[i*2],z[i*2+1],z[i*2+2],z[i*2+3]
      m = (y2-y1)/(x2-x1)
      b = y1-m*x1
      y = min(y1,y2)//a*a+a
      while y < max(y1,y2):
         x = (y-b)//m
         points += (x,y)
         y += a
   x,y = [],[]
   for i in range(len(points)//2):
      x.append(points[i*2])
      y.append(points[i*2+1])
   setColor(c[0],c[1],c[2])
   for k in range(len(y)):
      for i in range(len(y)):
         if y[k] == y[i] and x[k] != x[i]:
            drawLine(x[k],y[k],x[i],y[i])
