#daydayup.py 天天向上的力量：工作日努力和每天努力
def dayup(df): #df 努力的系数，如每天进步1%，df=0.01
    dayup=1
    for i in range(365):
        if i%7 in[6,0]: #判断是否是星期六和星期天
            dayup = dayup * (1-0.01) #周六日下降1%
        else:
            dayup = dayup *(1+df)
    return dayup
dayfactory=0.01
while dayup(dayfactory) <37.78:
    dayfactory +=0.001
print("工作日努力的参数是：{:.3f}".format(dayfactory))


