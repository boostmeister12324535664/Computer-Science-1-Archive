# KeyboardInput07.py
# This program demonstrates the issues that arise
# when you try to use <input> in a graphics program.
# One issue is the graphics window covers the input.
# A bigger issue is that the input may be unending
# depending on your version of Python.


from Graphics import *

beginGrfx(1300,700)

myColor = input("Enter any color name.  -->  ")
myRadius = eval(input("Enter a radius value from 1-300.  -->  "))

setColor(myColor)
fillCircle(650,350,myRadius)

endGrfx()
