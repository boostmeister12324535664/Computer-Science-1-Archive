# Lab09Bst.pv
# "Geometry Functions"
# This is the student, starting version of Lab 09B.


from math import pi


def heading():
   print()
   print("**********************************")
   print("Lab 09B, Geometry Functions")
   print("100 Point Version")
   print("By: GABRIEL NGUYEN") # Substitute your own name here.
   print("**********************************")
   print("\n")


# 2D Perimeters
def squarePerimeter (s):
   return 4 * s
def pentagonPerimeter(x):
   return 5*x
def hexagonPerimeter(x):
   return 6*x
def octagonPerimeter(x):
   return 8*x
def rectanglePerimeter(x,y):
   return 2*(x+y)
def circleCircumference(x):
   return 2*x*pi

# 2D Areas
def rectangleArea (L,W):
   return L * W
def squareArea(x):
   return x**2
def parallelogramArea(x,y):
   return x*y
def triangleArea(x,y):
   return x*y/2
def trapezoidArea(x,y,z):
   return (x+y)*z/2
def hexagonArea(x,y,z):
   return (x+y)*z
def circleArea(x):
   return pi*x**2

# 3D Surface Areas
def cubeSurfaceArea (s):
   return 6 * s ** 2
def squarePrismSurfaceArea(x,y):
   return 2*x**2+4*x*y   
def rectangularPrismSurfaceArea(x,y,z):
   return 2*x*y+2*y*z+2*x*z
def sphereSurfaceArea(x):
   return 4*pi*x**2



# 3D Volumes
def cylinderVolume (r,h):
   return pi * r ** 2 * h
def cubeVolume(x):
   return x**3
def squarePrismVolume(x,y):
   return x**2*y
def rectangularPrismVolume(x,y,z):
   return x*y*z
def pyramidVolume(x,y):
   return x**2*y/3
def coneVolume(x,y):
   return pi*x**2*y/3
def sphereVolume(x):
   return pi*x**3*4/3



	


##########
#  MAIN  #
##########

heading()

side   =  10.0
length =  20.0
width  =  30.0
height =  40.0
base1  =  60.0
base2  =  80.0
radius = 100.0

# Uncomment the print statements below as you complete each of the functions.
# Leave hashtags in place for any functions that you have not yet finished.

print("Perimeters of 2D Shapes")
print("=====================================================")
print("Square Perimeter:               ",squarePerimeter(side))
print("Pentagon Perimeter:             ",pentagonPerimeter(side))
print("Hexagon Perimeter:              ",hexagonPerimeter(side))
print("Octagon Perimeter:              ",octagonPerimeter(side))
print("Rectangle Perimeter:            ",rectanglePerimeter(length,width))
print("Circle Circumference:           ",circleCircumference(radius))
print("\n")
print("Areas of 2D Shapes")
print("=====================================================")
print("Square Area:                    ",squareArea(side))
print("Rectangle Area:                 ",rectangleArea(length,width))
print("Parallelogram Area:             ",parallelogramArea(base1,height))
print("Triangle Area:                  ",triangleArea(base1,height))
print("Trapezoid Area:                 ",trapezoidArea(base1,base2,height))
print("Hexagon Area:                   ",hexagonArea(base1,base2,height))
print("Circle Area:                    ",circleArea(radius))
print("\n")
print("Surface Areas of 3D Shapes")
print("=====================================================")
print("Cube Surface Area:              ",cubeSurfaceArea(side))
print("Square Prism Surface Area:      ",squarePrismSurfaceArea(side,height))
print("Rectangular Prism Surface Area: ",rectangularPrismSurfaceArea(length,width,height))
print("Sphere Surface Area:            ",sphereSurfaceArea(radius))
print("\n")
print("Volumes of 3D Shapes")
print("=====================================================")
print("Cube Volume:                    ",cubeVolume(side))
print("Square Prism Volume:            ",squarePrismVolume(side,height))
print("Rectangular Prism Volume:       ",rectangularPrismVolume(length,width,height))
print("Pyramid Volume:                 ",pyramidVolume(side,height))
print("Cylinder Volume:                ",cylinderVolume(radius,height))
print("Cone Volume:                    ",coneVolume(radius,height))
print("Sphere Volume:                  ",sphereVolume(radius))
print()
