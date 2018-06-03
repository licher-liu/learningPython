import turtle
def Rect(width,hight,x,y,color):
    turtle.pencolor(color)
    turtle.speed(5000)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(2):
        turtle.fd(width)
        turtle.right(90)
        turtle.fd(hight)
        turtle.right(90)

def main():
    turtle.setup(600,600)
    RectWidth=10
    RectHight=10
    RectX=0
    RectY=0
    Gap=10
    Rectcolor=(0,0.5,1)
    Rect(RectWidth,RectHight,RectX,RectY,Rectcolor)
    for i in range(15):
        RectWidth=RectWidth+Gap*2
        RectHight=RectHight+Gap*2
        RectX=RectX-Gap
        RectY=RectY+Gap
        Rect(RectWidth,RectHight,RectX,RectY,Rectcolor)
    turtle.done()


main()
