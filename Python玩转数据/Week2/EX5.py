#异常处理 可以用循环，输入错误后还可以继续尝试
while True:
    try:
        num1 = int(input('Enter the first number:'))
        num2 = int(input('Enter the second number:'))
        print(num1/num2)
      #  break
    except Exception as err:
        print('something is wrong!')
        print(err) #输出错误原因
    else:
        print('you get your result')
        break
    finally:
        print('************finally always run************')
