age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('name={0} and age={1}'.format(name,age))
# 用\n 来换行打印
print('{0}\n{1}'.format(age,name))
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}   {1:.2f}'.format(1.0/3,2/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:*^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
#print 总是会以一个不可见的“新一行”字符（ \n ）为防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾
print('a', end=' ')
print('b', end=' ')
print("This is the first sentence.\ This is the second sentence.")
print('\'asfd\' ') #打印' " 在前面加\
