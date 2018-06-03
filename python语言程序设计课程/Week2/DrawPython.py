import turtle
#绘制一条蟒蛇
turtle.setup(650,350,200,200) #设置画板大小
turtle.penup() #画笔提起
turtle.fd(-250) #向后移动250
turtle.pendown() #画笔落下
turtle.pencolor("purple") #改变笔的颜色
turtle.pensize(25) #改变笔的粗细
turtle.seth(-40) #改变海龟的朝向
for i in range(4):
    turtle.circle(40,80) #画圆弧
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40) #向前走画线
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()


