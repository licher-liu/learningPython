#字符串的方法
# str.low() 返回小写 str.upper()返回大写
a='abc'
print(a.lower())
print(a.upper())
# str.split(sep=None) 返回一个列表，由str根据sep被分割的部分组成
b='A,B,Cd'
print(b.split(','))
print(b.count('A'))
c='python'
print(c.replace('n','*****'))
#居中，空白处填充字符
print(c.center(20,'='))
#.strip去掉左侧右侧的制定字符
print(c.strip(' =np'))
#join 增加一个str
d=','
print(d.join('123'))
