# TextFiles21.py
# This program demonstrates that data from a 
# text file can be used in a graphics program.


from Graphics import *


file = open("TextFiles21.txt",'r')

x1 = int(file.readline())
y1 = int(file.readline())
r1 = int(file.readline())
x2 = int(file.readline())
y2 = int(file.readline())
r2 = int(file.readline())
x3 = int(file.readline())
y3 = int(file.readline())
r3 = int(file.readline())
x4 = int(file.readline())
y4 = int(file.readline())
r4 = int(file.readline())
x5 = int(file.readline())
y5 = int(file.readline())
r5 = int(file.readline())
x6 = int(file.readline())
y6 = int(file.readline())
r6 = int(file.readline())
r7 = int(file.readline())

file.close()

beginGrfx(1000,650)

drawCircle(x1,y1,r1)
drawCircle(x2,y2,r2)
drawCircle(x3,y3,r3)
fillCircle(x4,y4,r4)
fillCircle(x5,y5,r5)
drawOval(x6,y6,r6,r7)

endGrfx()