#使用turtle库，绘制一个同切圆
import turtle as tt
tt.setup(650,450,300,100) #setup(长，高，屏幕左边坐标，屏幕右边坐标
tt.penup()
tt.goto(0,-100)
tt.pendown()
for i in range(4):
    tt.circle(i*20+60,360)

tt.done()
