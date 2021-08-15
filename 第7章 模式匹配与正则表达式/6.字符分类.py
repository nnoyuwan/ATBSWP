# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/12 11:42 下午

# 在前面电话号码正则表达式的例子中，你知道\d 可以代表任何数字。
# 也就是说，\d 是正则表达式(0|1|2|3|4|5|6|7|8|9)的缩写。有
# 许多这样的“缩写字符分类”
# \d 0到9的任何数字
# \D 除了0到9数字以外的任何字符
# \w 任何字母、数字或下划线字符（可以认为是匹配"单词"的字符）
# \W 除字母、数字和下划线以外的任何字符
# \s 空格、制表符或换行符（可以认为是匹配"空白"字符）
# \S 除空格、制表符和换行符以外的任何字符

# 字符分类对于缩短正则表达式很有用。字符分类[0-5]只匹配数字 0 到 5，
# 这比 输入(0|1|2|3|4|5)要短很多。
import re
xmasRegex = re.compile(r'\d+\s\w+') # 一个或多个数字 + 空白 + 一个或多个字符
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
