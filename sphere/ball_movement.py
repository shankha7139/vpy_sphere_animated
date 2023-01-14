from vpython import *
from time import *
flooor=box(pos=vector(0,-5,0),color=color.cyan,size=vector(10,0.1,10))
ceiling=box(pos=vector(0,5,0),color=color.cyan,size=vector(10,0.1,10))
w1=box(pos=vector(-6,0,0),color=color.cyan,size=vector(.1,10,10))
w2=box(pos=vector(6,0,0),color=color.cyan,size=vector(.1,10,10))
w3=w1=box(pos=vector(0,0,-6),color=color.cyan,size=vector(10,10,0.1))
ball=sphere(color=color.red,pos=vector(0,0,0),radius=0.5)
deltax=.1
xpos=0
while True:
    rate(200)
    xpos=xpos+deltax
    if abs(xpos)>6:
        deltax=deltax*(-1)    
    ball.pos=vector(xpos,0,0)
