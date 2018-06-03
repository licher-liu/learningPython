def say_hello():
    # 该块属于这一函数
    print("hello world")
# 函数结束


times = int(input('how many times do you want print:'))
for i in range(0, times):
    # 调用函数
    say_hello()


