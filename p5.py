import turtle
import math,random,os

os.system("cls")
print('''
     /\           
    /__\  |) |_| | |/
   /    \ |) | | | |\ 
                  

''')
# setup the screen
wn=turtle.Screen()
wn.bgcolor("#00ff5e")
wn.bgpic("rrRCNyt.gif")
wn.tracer(2)

# draw border
maborder=turtle.Turtle()
maborder.color("#e3e3e3")
maborder.penup()
maborder.setposition(-300,-300)
maborder.pendown()
maborder.pensize(5)
maborder.speed(5)
for i in range(4):
    maborder.fd(600)
    maborder.left(90)
maborder.hideturtle()


# player
player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

# create goal
maxgoal=6
goals=[]
for count in range(maxgoal):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
# set speed var
speed=1
socrates=0

# define funcs
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global speed
    speed+=1
def decreasespeed():
    global speed
    if speed>0:
        speed-=1
    else:
        speed=0
def isCollision(t1,t2):
    global socrates
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    # print(d)
    # 19.876388488340947
    if d<20:
        return True
    else:
        return False

# set keyboard bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")

while True:
    
    player.fd(speed)

    #boundary checkin playa
    if player.xcor()>300 or player.xcor()<-300:
        player.right(180)
    elif player.ycor()>300 or player.ycor()<-300:
        player.right(180)
    
    
    # collision detect
    

    for count in range(maxgoal):
        goals[count].fd(2)
        #boundary checkin goal
        if goals[count].xcor()>290 or goals[count].xcor()<-290:
            goals[count].right(180)
        elif goals[count].ycor()>290 or goals[count].ycor()<-290:
            goals[count].right(180)
        
        if isCollision(player,goals[count]):
        
            goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            socrates+=10
            print(socrates)
            # draw score on screen
            maborder.undo()   #helps in avoiding overwriting score
            maborder.penup()
            maborder.hideturtle()
            maborder.setpos(-290,305)
            scorestring="SCORE is : {}".format(socrates)
            maborder.write(scorestring,False,align="left",font=("Arial",14,"normal"))


    
# print(socrates)




















