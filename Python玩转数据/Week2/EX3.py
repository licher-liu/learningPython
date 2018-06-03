#处理多个异常
try:
    num1 = int(input('Enter the first number:'))
    num2 = int(input('Enter the second number:'))
    print(num1/num2)
except ValueError:
    print('please input a digit')
except ZeroDivisionError as err:
    print('The second number cannot be zero')
    print(err)
#或者
except(ValueError,ZeroDivisionError):
    print('invalid input!')

