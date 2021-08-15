# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/13 12:14 上午

# 可以在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处。
# 类似地，可以再正则表达式的末尾加上美元符号（$），表示该字符串必须以这个正则表达式的模式结束。

# 可以同时使用^和$，表明整个字符串必须匹配该模式，也就是说，只匹配该字符串的某个子集是不够的
import re

beginWithHello = re.compile(r'^Hello')
beginWithHello.search('Hello World!')
print(beginWithHello.search('He said hello') is None)

# 正则表达式 r'\d$'匹配以数字 0 到 9 结束的字符串。
endWithNumber = re.compile(r'\d$')
endWithNumber.search('Your number is 42')
print(endWithNumber.search('Your number is forty two') is None)

# 正则表达式 r'^\d+$'匹配从开始到结束都是数字的字符串。
wholeStringNumber = re.compile(r'^\d+$')
wholeStringNumber.search('1234567890')
print(wholeStringNumber.search('12345xyz67890') is None)
print(wholeStringNumber.search('123 4567890') is None)

# 我总是会混淆这两个符号的含义，所以我使用助记法“Carrots cost dollars”，
# 提醒我插入符号在前面，美元符号在后面。
