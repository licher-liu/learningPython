#字符串操作
#输入1-7的数字，打印星期几 采用字符串连接
weekStr='一二三四五六日'
weekId=eval(input('请输入星期数字（1-7）：'))
print('星期'+weekStr[weekId-1])
