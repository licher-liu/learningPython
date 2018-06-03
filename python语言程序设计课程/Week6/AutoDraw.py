#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#读取数据
datals = []
f = open("data.txt")
for line in f:
    line= line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
f.close()

#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5]) # 3 4 5 参数为颜色
    t.fd(datals[i][0]) #0号参数为前进多少距离
    if datals[i][1]: #1号参数 =1 右转 =0 左转
        t.right(datals[i][2]) #2 号参数转的角度
    else:
        t.left(datals[i][2]) #2 号参数转的角度
t.done()

