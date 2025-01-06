### BACKGROUND ###

from DrawingProcedures import *



def drawBackground():
   color('blue4')
   fillRectangle(0,0,1300,700)
   x = randint(0,3)
   if x == 1:
      color('red')
      fillPolygon([580,255, 530,290, 523,280, 521,270, 520,260])
      for i in range(0,20):
         lerpLine(randint(0,1300),randint(0,700),randint(0,1300),randint(0,700),randint(30,100),randint(50,100))
   for a in range(5):
      pp = []
      width(randint(3,5))
      for i in range(randint(5,10)):
         pp += (randint(0,1300),randint(0,700))
         while pp.count(pp[-2]) > 1:
            pp[-2] = randint(0,1300)
      Lp(pp,randint(10,17),[randint(1,255),randint(1,255),randint(1,255)])