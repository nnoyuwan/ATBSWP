# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/9 4:58 下午

# 6.1.1
# 在 Python 中输入字符串值相当简单的：它们以单引号开始和结束。
# 但是如何才 能在字符串内使用单引号呢？

# spam = 'That is Alice's cat' # str在Alice处就结束了

# 6.1.2 双引号
spam = "That is Alice's cat"
# 但是，如果在字符串中既要使用单引号又要使用双引号那就要使用转义字符。
spam = 'Say hi to Bob\'s mother.'

# 6.1.3 转义字符
# \'  单引号
# \"  双引号
# \n  换行符
# \t  制表符
# \\  倒斜杠

# 6.1.4 原始字符串可以在字符串开始的引号之前加上r，
# 使它成为原始字符串。“原始字符串”完 全忽略所有的转
# 义字符，打印出字符串中所有的倒斜杠。

print(r'That is Carol\'s cat.')  # That is Carol\'s cat.

# 6.1.5 用三重引号的多行字符串
# 虽然可以用\n 转义字符将换行放入一个字符串，但使用多行字符串通常更容易。
# 在 Python 中，多行字符串的起止是 3 个单引号或 3 个双引号。“三重引号”
# 之间的 所有引号、制表符或换行，都被认为是字符串的一部分。

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary,

and extortion.
Sincerely
Bob''')

# 请注意，Eve's 中的单引号字符不需要转义。在原始字符串中，
# 转义单引号和双引号是可选的。下面的 print()调用将打印出
# 同样的文本，但没有使用多行字符串：
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

# 6.1.6 多行注释
# 虽然井号字符（#）表示这一行是注释，但多行字符串常常用作多行注释。
# 下面是完全有效的 Python 代码：
"""This is a test Py thon pro g ram.

Written by A l Sweiga rt al@in v entwithpytho n.com

This program was des igned fo r Python 3, n ot Pytho n 2."""


def spam():
    """This is a mul tiline c o mment to hel p explain what the spam() f unction does ."""
    print('H ello!')


# 6.1.7 字符串下标和切片
spam = 'Hello World!'
spam[0]
spam[4]
spam[-1]
spam[0:5]
spam[:5]
spam[6:]

# 6.1.8 字符串的 in 和 not in 操作符
'Hello' in 'Hello World'
'HELLO' in 'Hello World'

'cats' not in 'cats and dogs'
