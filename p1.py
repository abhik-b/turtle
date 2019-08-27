import turtle
# squaRES
ab=turtle.Turtle()
ab.color("#151515","#00ff5e")
for i in range(3):
    ab.begin_fill()
    ab.forward(100)
    ab.left(90)
    ab.forward(100)
    ab.left(90)
    ab.forward(100)
    ab.left(90)
    ab.forward(100)
    ab.left(90)
    
    ab.end_fill()

    ab.penup()
    ab.forward(10)
    ab.pendown()
    i-=1

# ab.begin_fill()
# ab.forward(100)
# ab.left(90)
# ab.forward(100)
# ab.left(90)
# ab.forward(100)
# ab.left(90)
# ab.forward(100)
# ab.left(90)
# ab.end_fill()
turtle.done()