# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/13 12:40 下午
import re

# 如果要匹配的文本模式很简单，正则表达式就很好。但匹配复杂的文本模式，
# 可能需要长的、费解的正则表达式。你可以告诉 re.compile()，忽略正则
# 表达式字符 串中的空白符和注释，从而缓解这一点。
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# 你可以将正则表达式放在多行中，并加上注释，像这样：
phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?               # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)?                      # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2, 5})?   # extension
)''', re.VERBOSE)

# 请注意，前面的例子使用了三重引号('")，创建了一个多行字符串。这样就可以 将正则表达式定义放在多行中，让它更可读。
#
# 正则表达式字符串中的注释规则，与普通的 Python 代码一样：#符号和它后面直到
# 行末的内容，都被忽略。而且，表示正则表达式的多行字符串中，多余的空白字符也
# 不认为是要匹配的文本模式的一部分。这让你能够组织正则表达式，让它更可读。

