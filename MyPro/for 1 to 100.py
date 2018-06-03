i=0
x=0
sum=0
for i in range(1,10):
    x=sum
    sum=sum+i
    print('{0}+{1}={2}'.format(x,i,sum))
   # print(x,'+',i,'=',sum)
  # print(x,"=",x,"+",i)

print('The for loop is over')
print('sum is ', x)

