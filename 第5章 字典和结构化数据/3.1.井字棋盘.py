# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/9 10:12 上午

# 因为 theBoard 变量中每个键的值都是单个空格字符，
# 所以这个字典表示一个完 全干净的棋盘。
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# 如果玩家 X 选择了中间的空格，就可以用下面这个字典来表示棋盘：
theBoard_1 = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
              'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
              'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# 一个玩家 O 获胜的棋盘上，他将 O 横贯棋盘的顶部，看起来像这样:
theBoard_2 = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
              'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
              'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# printBoard(theBoard)
# printBoard(theBoard_1)
# printBoard(theBoard_2)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move to which space?')
    move = input()
    theBoard[move] = turn
    turn = 'X' if turn == 'O' else 'O'
