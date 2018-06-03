def factorial(number):
    product = 1
    for i in range(number):
        product = product*(i+1)
    return product
# 采用递归的方式编写阶乘函数


def factorial1(number1):
    if number1 <= 1:
        return 1
    else:
        return number1*factorial1(number1-1)


a = eval(input("input a number:"))
print(factorial1(a))
