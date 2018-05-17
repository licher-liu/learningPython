
#从AutoDrawData.txt文件读取数据数据绘制图形文件格式如下：
# #号开头为注释文字
# A,B,C,D,E,F   :
#A =0 左转 =1 右转
#B 转的角度
#C =300  前进300像素距离
#D,E,F RGB三种颜色''''
# import turtle as t
t.title("自动绘制")
t.setup(1024,768)
t.pencolor("red")
t.pensize(1)
t.goto(0,0)
t.speed(0)
t.Turtle().screen.delay(0)
#读取数据文件 数据文件有中文注释，采用UTF-8 编码
trace=[]
f=open("AutoDrawData.txt",encoding="utf-8")
for line in f:
    line=line.replace("\n","")
    if len(line)>0: #防止数据文件空行
        if line[0] =="#":
            continue
        else:
            trace.append(list(map(eval,line.split(","))))
f.close()

for i in range(len(trace)):
    t.pencolor(trace[i][3],trace[i][4],trace[i][5])
    if trace[i][0] ==0:
        t.left(trace[i][1])
    else:
        t.right(trace[i][1])
    t.fd(trace[i][2])

t.done()
