import turtle
import math

# rotatin circle
ab=turtle.Turtle()
ab.color("#151515","white")
ab.speed(20)
ab.begin_fill()
for i in range(500):
    ab.fd(math.sqrt(i)*10)
    ab.left(170)
    
ab.end_fill()

turtle.done()