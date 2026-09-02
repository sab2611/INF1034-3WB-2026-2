
from turtle import *

t = Turtle()
#t.shape("turtle")

t.pu()
t.goto(-400, 0)
t.pd()
t.goto(400, 0)
t.stamp()

t.pu()
t.goto(0, -400)
t.pd()
t.goto(0, 400)
t.pd()
t.lt(90)
t.stamp()
t.rt(90)

#for cont in range(4):
    # print(cont)
 #   t.fd(100)
  #  t.lt(90)

t.pu()
t.goto(150, 300)
t.pd()
for cont in range(8):
    t.fd(100)
    t.rt(45)

t.pu()
t.goto(150, -300)








mainloop()