# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/10 12:24 上午

def printPicnic(itemDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# 6.2.6 用 strip()、rstrip()和 lstrip()删除空白字符
# strip()字符串方法将返回一个新的字符串，它的开头或末尾
# 都没有空白字符。 lstrip()和 rstrip()方法将相应删除左
# 边或右边的空白字符。
spam = '  Hello World '
lstrip = spam.lstrip()
lstrip
rstrip = spam.rstrip()
rstrip
strip = spam.strip()
print(strip)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam_strip = spam.strip('ampS')
# 删除出现的 a、m、p 和大写的 S。传入 strip()方法的字符串中，
# 字符的顺序并不重要：strip('ampS') 做的事情
# 和 strip('mapS')或 strip('Spam')一样。

# 6.2.7 用pyperclip模块拷贝粘贴字符串
# perclip 模块有 copy()和 paste()函数，可以向计算机的剪贴板发送文本，
# 或从 它接收文本。将程序的输出发送到剪贴板，使它很容易粘贴到邮件、文字
# 处理程序 或其他软件中。
import pyperclip

pyperclip.copy('Hello world!')
pyperclip.paste()

# 当然，如果你的程序之外的某个程序改变了剪贴板的内容，
# paste()函数就会返回它。
