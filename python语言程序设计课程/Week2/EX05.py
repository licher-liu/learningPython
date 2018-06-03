"""长度转换 I
描述
请编写程序，完成米和英寸之间的长度转换，基本需求如下：
输入英寸，转换成米；
输入米，转换成英寸。
英寸采用in标记，放在数值结尾；米采用m标记，放在数值结尾。
1 米 = 39.37 英寸
输入参数请使用input()，不要增加提示字符串信息。"""
Dis = input()
if Dis[-2:] in ['in', 'IN']:
    meter = eval(Dis[:-2]) / 39.37
    print("{0:.3f}m".format(meter))
if Dis[-1:] in ['m', 'M']:
    inch = eval(Dis[:-1]) * 39.37
    print("{0:.3f}in".format(inch))
# else:
#        print("input error")
