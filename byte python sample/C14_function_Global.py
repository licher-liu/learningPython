x = 50

"""
如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还
是类），那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的。我们需要通
过 global 语句来完成这件事
"""

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)
