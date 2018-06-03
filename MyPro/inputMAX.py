
# int(input('Enter an integer : '))
numberlist=[]
print('')
while True:
    UserInput=input('please in put your numbers ,type done to end:')
    if UserInput.isnumeric():
        numberlist.append(int(UserInput))
    elif  UserInput =='done':
        break
    else:
        print('please input a number')


print(numberlist)

