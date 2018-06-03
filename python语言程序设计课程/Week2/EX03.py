#使用turtle库，绘制一个叠边形，其中，叠边形内角为80度。
import turtle as tt
tt.setup(650,450,300,100) #setup(长，高，屏幕左边坐标，屏幕右边坐标
tt.penup()
tt.goto(-100,-100)
tt.pendown()
for i in range(9):
    tt.fd(100)
    tt.left(80)
tt.done()
