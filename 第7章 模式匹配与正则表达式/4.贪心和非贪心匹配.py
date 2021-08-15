# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/12 8:54 下午
import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()  # Out[43]: 'HaHaHaHaHa'

# 你可能 会想，为什么在前面花括号的例子中，Match 对象的 group()
# 调用会返回'HaHaHaHaHa'， 而不是更短的可能结果。毕竟，'HaHaHa'
# 和'HaHaHaHa'也能够有效地匹配正则表达 式(Ha){3,5}。

# 因为Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们
# 会尽可能匹配最长的字符串。

# 非贪心策略只需在花括号后面加一个？

greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()  # Out[43]: 'HaHaHa'

# 注意，问号在正则表达式中可能有两种含义：
# 1.声明非贪心匹配 ?在{}之后
# 或
# 2.表示可选的分组。?在()之后
# 这两种含义是完全无关的。
