import turtle
import math,os
os.system("cls")
print('''
     /\           
    /__\  |) |_| | |/
   /    \ |) | | | |\ 
                  

''')
# rotatin circle
ab=turtle.Turtle()
ab.color("#1eabc9")
ab.speed(50)
ab.begin_fill()
for i in range(500):
    ab.fd(math.sqrt(i)*10)
    ab.left(170)
    
ab.end_fill()
ab.penup()
ab.setpos(-55,-250)
ab.write("ABHIK",False,align="left",font=("Arial", 30, "normal"))
ab.hideturtle()
turtle.done()