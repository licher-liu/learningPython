#单行刷新文本进度条完整效果
import time
scale = 50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a = '*'* i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur =time.perf_counter()-start
    print("\r{0:^3.0f}%[{1}-->{2}]{3:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
