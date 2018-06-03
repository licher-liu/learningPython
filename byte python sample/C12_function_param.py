def print_max(a, b):
    if a > b:
        print('number a is {0},number b is {1}:'.format(a, b), a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print('number a is {0},number b is {1}:'.format(a, b),b, 'is maximum')
# 直接传递字面值


print_max(3, 4)
x = 7
y = 5
# 以参数的形式传递变量
print_max(x, y)
