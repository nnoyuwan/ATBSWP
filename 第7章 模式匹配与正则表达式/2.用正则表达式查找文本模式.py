# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/11 11:38 下午


# 7.2.1 创建正则表达式对象
import re

# \d表示"一个数字字符"
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# 7.2.2 匹配 Regex 对象

# search()方法将返回一个Match对象。Match对象有一个group()方法，
# 它返回被查找字符串中实际匹配的文本（稍后我会解释分组）。
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

#               向 re.compile()传递原始字符串
#   回忆一下，Python 中转义字符使用倒斜杠（\）。字符串'\n'表示一个换行字符，
# 而不是倒斜杠加上一个小写的 n。你需要输入转义字符\\，才能打印出一个倒斜杠。
# 所以'\\n'表示一个倒斜杠加上一个小写的 n。但是，通过在字符串的第一个引号之
# 前加上 r，可以将该字符串标记为原始字符串，它不包括转义字符。
#   因为正则表达式常常使用倒斜杠，向 re.compile()函数传入原始字符串就很方
# 便 ， 而 不 是 输 入 额 外 得 到 斜 杠 。 输 入 r'\d\d\d-\d\d\d-\d\d\d\d' ， 比输入
# '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'要容易得多。

# 7.2.3 正则表达式匹配复习

# 虽然在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
# 1．用 import re 导入正则表达式模块。
# 2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
# 3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
# 4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串
