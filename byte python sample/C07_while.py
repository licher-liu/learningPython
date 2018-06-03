number=23
running=True
while running:
    guess=int(input('enter an integer'))
    if guess == number:
        print('Congratulations, you guessed it.the number is ' ,number)
        # 这将导致 while 循环中止
        running = False
    elif guess< number:
        print('No, it is a little higher than {0}.'.format(guess))
    else:
        print('No, it is a little lower than {0}.'.format(guess))
else:
    print('The while loop is over.')
    # 在这里你可以做你想做的任何事
print('Done')
