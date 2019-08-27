from turtle import *
import math,os
os.system("cls")
print('''
     /\           
    /__\  |) |_| | |/
   /    \ |) | | | |\ 
                  

''')
color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     # if abs(pos()) < 1:
#     #     break
# end_fill()
# done()

begin_fill()
for i in range(16):
    fd(200)
    right(170)
    # if abs(pos())<1:
    #     break
end_fill()
done()