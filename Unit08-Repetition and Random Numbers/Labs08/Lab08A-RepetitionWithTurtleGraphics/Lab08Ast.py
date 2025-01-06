# Lab08Ast.py
# "Repetition with Turtle Graphics"
# This is the student, starting version of Lab 08A.
# After completing each shape, student need to "un-comment"
# the 4 commands which follow before they start the next shape.


from turtle import * 
from time import sleep

setup(1300,700)
tracer(0,0) 


def p(x):
   if x == 0:
      penup()
   else:
      pendown()

def f(x):
   forward(x)

def r(x):
   right(x)
   
def l(x):
   left(x)
   
def c(x):
   color(x)
   
def w(x):
   width(x)

#########################################      
#  Diagonal Initials  -  50 Points      #
#=======================================#
#  In order to receive credit, you      #
#  must have at least FOUR sets of      #
#  YOUR initials displayed diagonally.  # 
#  The initials must be evenly spaced   #
#  and a <for> loop must be used.       #
#########################################


p(0)
f(-450)
l(90)
f(250)
r(90)

for i in range(5):
   p('G')
   l(90)
   f(25)
   l(90)
   f(60)
   l(90)
   f(100)
   l(90)
   f(60)
   l(90)
   f(40)
   r(90)
   f(20)
   p(0)
   f(30)
   r(90)
   f(40)
   p('A')
   f(-100)
   l(30)
   f(115)
   l(150)
   f(100)
   p(0)
   f(-120)
   r(90)
   f(100)



update() 
sleep(1)
reset()
tracer(0,0)

   
#######################
#  Solid Red Octagon  #
#######################

c('red')
begin_fill()
for i in range(8):
   f(100)
   l(45)
end_fill()

 

update() 
sleep(1)
reset()
tracer(0,0)



###################
#  15 Point Star  #
###################

for i in range(16):
   f(250)
   r(168)




update()
sleep(1)
reset()
tracer(0,0)



###############
#  Plus Sign  #
###############

for i in range(4):
   f(100)
   r(90)
   f(75)
   r(90)
   f(100)
   l(90)


  

update()
sleep(1)
reset()
tracer(0,0)



############################################
#  Big Thick Snowflake with 2 Thin Babies  #
############################################

y = 150

def sf():
   p('B')
   for i in range(9):
      f(y)
      f(-y)
      r(40)
   p(0)
   
p(0)
f(-500)
sf()
f(1000)
sf()
f(-500)
w(20)
y = 300
sf()

      




update()
sleep(1)
reset()
tracer(0,0)


############
#  Circle  #
############


for i in range(360):
   f(2)
   r(1)



update()
sleep(1)
reset()
tracer(0,0)


########################
#  Horizontal Zig-Zag  #
########################

p(0)
f(-600)
r(90)
f(330)
l(90)
p('R')

for i in range(10):
   f(1200)
   l(90)
   f(30)
   l(90)
   f(1200)
   r(90)
   f(30)
   r(90)
f(1200)
l(90)
f(30)
l(90)
f(1200)



update()
sleep(1)
reset()
tracer(0,0)


##################
#  Cool Pattern  #
##################

p(0)

for i in range(120):
   f(200)
   p('I')
   r(90)
   f(200)
   f(-400)
   f(200)
   l(90)
   p(0)
   f(-200)
   r(3)




update() 
sleep(1)
reset()
tracer(0,0)


##########################
#  Flower of 12 Squares  #
##########################

for i in range(3):
   for i in range(4):
      for i in range(4):
         f(200)
         r(90)
      l(90)
   l(30)

   



update()
sleep(1)
reset()
tracer(0,0)



##########################
#  Flower of 10 Circles  #
##########################

for i in range(10):
   for i in range(360):
      f(2)
      r(1)
   l(36)




update()
sleep(1)
reset()
tracer(0,0)


#####################
#  Westbound Comet  #
#####################

f(-500)
ww = 200
for i in range(200):
   w(ww)
   f(5)
   ww -= 1


update()
sleep(1)
reset()
tracer(0,0)


################
#  Box Spiral  #
################

v = 25

for i in range(25):
   f(v)
   r(90)
   v += 25




update()
sleep(1)
reset()
tracer(0,0)



####################################
#  Triple Nested Golden Honeycomb  #
####################################



c('gold')

p(0)
f(-590)
l(90)
f(300)
r(90)
for i in range(3):
   for i in range(3):
      p('E')
      begin_fill()
      for i in range(6):
         f(90)
         r(60)
      end_fill()
      p(0)
      r(90)
      f(200)
      l(90)
   f(180)
   l(90)
   f(500)
   r(90)
   for i in range(2):
      p('E')
      begin_fill()
      for i in range(6):
         f(90)
         r(60)
      end_fill()
      p(0)
      r(90)
      f(200)
      l(90)
   l(90)
   f(500)
   r(90)
   f(180)
for i in range(3):
      p('E')
      begin_fill()
      for i in range(6):
         f(90)
         r(60)
      end_fill()
      p(0)
      r(90)
      f(200)
      l(90)




update()
done()