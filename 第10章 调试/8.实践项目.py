# 下面程序的意图是一个简单的硬币抛掷猜测游戏。玩家有两次猜测机会（这
# 是一个简单的游戏）。但是，程序中有一些缺陷。让程序运行几次，找出缺陷，使
# 该程序能正确运行。

import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
toss = 'heads' if toss == 1 else 'tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # guesss = input()
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
