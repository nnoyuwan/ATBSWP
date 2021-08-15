# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/12 9:42 下午

# 除了 search 方法外，Regex 对象也有一个 findall()方法。

# 1.search()将返回一个 Match 对象，包含被查找字符串中的“第一次”匹配的文本

# 2.而findall()方字符串，包含被查找字符串中的所有匹配。
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
s = 'Cell: 415-555-9999 Work: 212-555-0000'
mo = phoneNumRegex.search(s)
mo.group()

phoneNumRegex.findall(s)  # findall()不是返回一个 Match 对象，而是返回一个字符串列表

# 如果在正则表达式中有分组，那么findall将返回元组的列表。
# 每个元组表示一个找到的匹配，其中的项就是正则表达式中每个分组的匹配字符串
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneNumRegex.findall(s)  # Out[51]: [('415', '555', '9999'), ('212', '555', '0000')]

# 作为 findall()方法的返回结果的总结，请记住下面两点：
# 1．如果调用在一个没有分组的正则表达式上，例如\d\d\d-\d\d\d-\d\d\d\d，
# 方法 findall()将返回一个匹配字符串的列表，
# 例如['415-555-9999', '212-555-0000']。
#
# 2．如果调用在一个有分组的正则表达式上，例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)，
# 方 法 findall()将返回一个字符串的元组的列表（每个分组对应一个字符串），
# 例如[('415', '555', '1122'), ('212', '555', '0000')]。