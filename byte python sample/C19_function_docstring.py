"""Python 有一个甚是优美的功能称作文档字符串（Documentation Strings），在称呼它时通常
会使用另一个短一些的名字docstrings。DocStrings 是一款你应当使用的重要工具，它能够帮
助你更好地记录程序并让其更加易于理解。令人惊叹的是，当程序实际运行时，我们甚至可
以通过一个函数来获取文档！"""
def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。
    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)

help(print_max)
