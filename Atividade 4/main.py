from turtle import *
from time import sleep
from random import *
t = Turtle ()

def desenha_plano_cartesiano():
    # Eixo dos X
    t.color('black')
    t.setheading(0)
    t.pu()
    t.goto(-300, 0)
    t.pd()
    t.goto(300, 0)
    t.stamp()
    # Eixo dos Y
    t.pu()
    t.goto(0, -300)
    t.pd()
    t.goto(0, 300)
    t.lt(90)
    t.stamp()

def desenha_1funçao(x):
    return x^3 - x^2 - x + 1

def desenha_2funçao(x):
    return x^2 - 5*x + 6


    #- y = √x (50XP)
    #- y = 1/x (50XP)
    #- y = 2^x (50XP)
    #- y = 5 - x^2 (75XP)
    #- y = x^2 - 5x + 6 (75XP)
    #- y = x^3 - x^2 - x + 1 (75XP)

#def corrida_tartaruga(x):
    #t(x).speed(0)
    #t(x)=pu()
    #t(X).goto(-200, 200)
    #t.pd()
#for num in range(30):
    #t(x).fd(randint(5,10))
    

#BP

desenha_plano_cartesiano()
t.pu()
t.color('blue')
t.goto(100, desenha_2funçao(-10))
for x in range(-100, 101):
    t.goto(2*x, desenha_2funçao(2*x))
t.pd()
t.clear()



desenha_plano_cartesiano()
t.pu()
t.color('red')
t.goto(-150, desenha_1funçao(90))
t.pd()
for x in range(-100, 101):
    t.goto(2*x, desenha_1funçao(2*x))
t.clear()



#corrida_tartaruga()




mainloop()