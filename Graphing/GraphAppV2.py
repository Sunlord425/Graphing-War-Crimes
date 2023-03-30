from math import *
import turtle as t
from random import *

def main():
    t.hideturtle()
    t.bgcolor("black")
    t.pencolor("white")
    t.penup()
    eq = t.textinput("equation","f(x) = ")
    t.colormode(255)
    xMod = t.textinput("X Mod","X Scaling: ")
    yMod = t.textinput("Y Mod","Y Scaling: ")

    x = 0
    y = 0
    fCoords = [x,y]
    rgb = [255,0,0]
    colorStep = 0
    start = [x,y]

    title = t.textinput("Title","Graph Title: ")
    canvW = int(t.numinput("canvW","Window Width: "))
    canvH = int(t.numinput("canvH","Window Height: "))
    zoom = float(t.numinput("Zoom","Zoom Value: "))
    res = 1/(float(t.numinput("GRes","Graph Resolution: ")))
    axisRes = int(t.numinput("ARes", "Axis Resolution "))

    t.screensize(canvW, canvH)

    t.tracer(0, 0)
    t.setposition(50, (canvH/2))
    t.write(title, align="left", font=('Arial', 20, 'normal'))
    t.home()
    t.pendown()
    t.setposition(canvW,0)
    t.setposition(-1*canvW,0)
    t.home()
    t.setposition(0,canvH)
    t.setposition(0,-1*canvH)
    t.pencolor(rgb[0],rgb[1],rgb[2])
    t.penup()
    
    t.setx(x)
    t.sety(eval(eq))

   ## t.dot(4)

    def forward(x, eq):
        try:
            y = eval(eq)
            return y
        except:
            pass

    def back(x,eq):
        try:
            y = eval(eq)
            return y
        except:
            pass

    
    while (abs(fCoords[0]) < canvW) and (abs(x) < 1000/res):
        if colorStep == 0:
            rgb[1] += 1
            if rgb[1] == 255:
                colorStep = 1
        elif colorStep == 1:
            rgb[0] -= 1
            if rgb[0] == 0:
                colorStep = 2
        elif colorStep == 2:
            rgb[2] += 1
            if rgb[2] == 255:
                colorStep = 3
        elif colorStep == 3:
            rgb[1] -= 1
            if rgb[1] == 0:
                colorStep = 4
        elif colorStep == 4:
            rgb[0] += 1
            if rgb[0] == 255:
                colorStep = 5
        elif colorStep == 5:
            rgb[2] -= 1
            if rgb[2] == 0:
                colorStep = 0
        t.pencolor(rgb[0],rgb[1],rgb[2])


        t.pendown()
        try:
            y = eval(eq)
            
        except:
            pass

        try:
            fCoords[0] = eval(xMod)*zoom
            fCoords[1] = eval(yMod)*zoom
        except:
            pass

        
        t.speed(0)
        t.setposition(fCoords[0],fCoords[1])
       

        x += res
        ##print(x)
    
    print("P done")
    t.penup()
    t.setx(start[0])
    t.sety(start[1])
    x = 0 
    colorStep = 0
    rgb = [255, 0, 0]
    fCoords = [0,0]
    while (abs(fCoords[0]) < canvW) and (abs(x) < 1000/res):

        if colorStep == 0:
            rgb[1] += 1
            if rgb[1] == 255:
                colorStep = 1
        elif colorStep == 1:
            rgb[0] -= 1
            if rgb[0] == 0:
                colorStep = 2
        elif colorStep == 2:
            rgb[2] += 1
            if rgb[2] == 255:
                colorStep = 3
        elif colorStep == 3:
            rgb[1] -= 1
            if rgb[1] == 0:
                colorStep = 4
        elif colorStep == 4:
            rgb[0] += 1
            if rgb[0] == 255:
                colorStep = 5
        elif colorStep == 5:
            rgb[2] -= 1
            if rgb[2] == 0:
                colorStep = 0
        t.pencolor(rgb[0],rgb[1],rgb[2])


        try:
            y = eval(eq)
        except:
            pass

        try:
            fCoords[0] = eval(xMod)*zoom
            fCoords[1] = eval(yMod)*zoom
        except:
            pass

        t.pendown()
        t.speed(0)
        t.setposition(fCoords[0],fCoords[1])
       

        x -= res
        ##print(x)

    print("N done")
    t.penup()
    t.color("white")
    offset = -20
    t.setposition(-1*canvW, offset)
    lastPos = [t.xcor(),t.ycor()]
    move = canvW/axisRes
    overlap = []
    for i in range(0, 2*axisRes):
        nover =True
        t.penup() 
        t.setposition((i*move)-canvW, offset)
        x = t.xcor()
        t.setposition(eval(xMod),  offset)
        for j in range (len(overlap)):
            if (abs(overlap[j] - t.xcor()) < 48):
                nover = False
        if (nover == True):
            t.write(round(x, 1)/zoom,)
            overlap.append(t.xcor())
    
    t.setposition(offset, -1*canvH)
    lastPos = [t.xcor(),t.ycor()]
    move = canvH/axisRes
    overlap = []
    for i in range(0, 2*axisRes):
        nover =True
        t.penup() 
        t.setposition(offset, (i*move)-canvH)
        y = t.ycor()
        t.setposition(offset, eval(yMod))
        for j in range (len(overlap)):
            if (abs(overlap[j] - t.ycor()) < 48):
                nover = False
        if (nover == True):
            t.write(round(y, 1)/zoom)
            overlap.append(t.ycor())

    t.update()
    t.done()

        
if __name__ == "__main__":
    main() 