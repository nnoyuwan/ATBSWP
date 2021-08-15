# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/13 1:24 下午

# 如果你希望在正则表达式中使用 re.VERBOSE 来编写注释，
# 还希望使用 re.IGNORECASE 来忽略大小写，该怎么办？
# 遗憾的是，re.compile()函数只接受一个值作为它的第二参数。
# 可以使用管道字符（|）将变量组合起来，从而绕过这个限制。
# 管道字符在这里称为“按位或”操作符。
import re

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

