import turtle,os
os.system("cls")
print('''
     /\           
    /__\  |) |_| | |/
   /    \ |) | | | |\ 
                  

''')
# sunflower
ab=turtle.Turtle()
ab.color("red","yellow")
ab.speed(10)
ab.begin_fill()
for i in range(44):
    ab.fd(200)
    ab.left(155.5)
    ab.fd(200)
ab.end_fill()
turtle.done()