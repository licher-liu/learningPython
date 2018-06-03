#异常处理 用空的except 语句处理所有异常
try:
    num1 = int(input('Enter the first number:'))
    num2 = int(input('Enter the second number:'))
    print(num1/num2)
except Exception as err:
    print('something is wrong!')
    print(err) #输出错误原因
else:
    print('you get your result')
