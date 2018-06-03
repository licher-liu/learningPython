#使用turtle库，绘制一个正方形。
import turtle as tt
tt.setup(650,450,300,100) #setup(长，高，屏幕左边坐标，屏幕右边坐标
for i in range(4):
    tt.fd(200)
    tt.left(90)
tt.done()
