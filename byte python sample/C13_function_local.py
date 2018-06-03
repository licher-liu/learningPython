"""局部变量
当你在一个函数的定义中声明变量时，它们不会以任何方式与身处函数之外但具有相同名称
的变量产生关系，也就是说，这些变量名只存在于函数这一局部（Local）。这被称为变量的
作用域（Scope）。所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始
"""
x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)
