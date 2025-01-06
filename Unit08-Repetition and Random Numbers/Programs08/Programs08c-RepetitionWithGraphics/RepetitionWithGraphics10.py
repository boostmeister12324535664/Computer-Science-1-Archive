# RepetitionWithGraphics10.py
# This program is similar to the previus program, but now
# the stars are filled in with solid colors. It also shows
# that <setColor> can be used with a single int parameter: 
# 0=Black, 1=Red, 2=Green, 3=Blue, 4=Orange, 5=Cyan, etc.
# Note that the radius <r> and number of points <p> variables
# are counting in the opposite direction from before.


from Graphics import *

beginGrfx(700,700)

x = 350
y = 350
r = 320
p = 14
c = 1

for k in range(5):
   setColor(c)
   fillStar(x,y,r,p)
   p -= 2
   r //= 2
   c += 1
endGrfx()  
 