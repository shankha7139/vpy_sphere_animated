from vpython import *
from time import *

srad=.5
wallthick=0.1
roomwidth=10
roomdepth=5
roomheight=10
flooor=box(pos=vector(0,-roomheight/2,0),color=color.cyan,size=vector(roomwidth,wallthick,roomdepth))
ceiling=box(pos=vector(0,roomheight/2,0),color=color.cyan,size=vector(roomwidth,wallthick,roomdepth))
wl=box(pos=vector(-roomwidth/2,0,0),color=color.cyan,size=vector(wallthick,roomheight,roomdepth))
wr=box(pos=vector(roomwidth/2,0,0),color=color.cyan,size=vector(wallthick,roomheight,roomdepth))
wb=box(pos=vector(0,0,-roomdepth/2),color=color.cyan,size=vector(roomwidth,roomheight,wallthick))
ball=sphere(color=color.red,pos=vector(0,0,0),radius=srad)

deltax=.1
xpos=0

deltay=.1
ypos=0

deltaz=.1
zpos=0

while True:
    rate(30)

    ypos-=deltay
    zpos-=deltaz
    xpos=xpos-deltax

    sr=xpos+srad
    sl=xpos-srad

    yt=ypos+srad
    yb=ypos-srad

    zb=zpos-srad
    zf=zpos+srad

    rwe=roomwidth/2-wallthick/2
    lwe=-roomwidth/2+wallthick/2
    cwe=roomheight/2-wallthick/2
    fwe=-roomheight/2+wallthick/2
    bwe=-roomdepth/2+wallthick/2
    frwe=roomdepth/2-wallthick/2
    
    if (sr>=rwe or sl<=lwe):
        deltax=deltax*(-1)   
    
    if (yt>=cwe or yb<=fwe):
        deltay=deltay*(-1)   

    if (zf>=frwe or zb<=bwe):
        deltaz=deltaz*(-1)       
    ball.pos=vector(xpos,ypos,zpos)
