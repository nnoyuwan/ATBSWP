# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/13 12:30 上午

# 在正则表达式中，.（句点）字符称为“通配符”。它匹配 除了换行 之外的所有字符。
# 例如，在交互式环境中输入以下代码：
import re

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# 要记住，句点字符只匹配一个字符，这就是为什么在前面的例子中，对于文本
# flat，只匹配 lat。要匹配真正的句点，就是用倒斜杠转义：\.。
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> fo r dinner . >')
mo.group()

# 点-星将匹配除换行外的所有字符。通过传入 re.DOTALL 作为
# re.compile()的第 二个参数，可以让句点字符匹配所有字符，包括换行字符。
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('a\nb').group()
noNewlineRegex = re.compile('.*', re.DOTALL)
noNewlineRegex.search('a\nb').group()
