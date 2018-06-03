'''同符号数学运算


描述
读入一个整数N，分别计算如下内容：
1. N的绝对值；
2. N与10进行同符号加法、减法和乘法运算，同符号运算指使用N的绝对值与另一个数进行运算，运算结果的绝对值被赋予N相同的符号，其中，0的符号是正号。
将上述4项结果在一行输出，采用空格分隔，输出结果均为整数'''
N=eval(input())
AbsN=abs(N)
if N<0:
    addN=-1*(abs(abs(N)+10))
    SubN=-1*(abs(abs(N)-10))
    MulN=-1*(abs(abs(N)*10))
else:
    addN=abs(abs(N)+10)
    SubN=abs(abs(N)-10)
    MulN=abs(abs(N)*10)
print(AbsN,addN,SubN,MulN)

