# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/13 10:50 上午

import re

# 通常，正则表达式用你指定的大小写匹配文本。
# 例如，下面的正则表达式匹配 完全不同的字符串：
regex1 = re.compile('Robocop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

# 但是，有时候你只关心匹配字母，不关心它们是大写或小写。
# 要让正则表达式不区分大小写，可以向re.compile()传入 re.IGNORECASE或 re.I，作为第二个参数。
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()
robocop.search('Al, why does your programming book talk about robocop so much?').group()
