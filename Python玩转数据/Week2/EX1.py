#FineName：Prime.py 打印2 到100 之间的素数
from math import sqrt
def isprime(x):
    if x==1:
        return False
    k=int(sqrt(x))  #为啥素数是在这个算法？
 #   print('k={}'.format(k))
    for j in range(2,k+1):
        if x%j==0:
            return False
    return True
for i in range(2,101):
    if isprime(i):
        print(i,end=' ')
