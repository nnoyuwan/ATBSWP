# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/12 11:50 下午

# 有时候你想匹配一组字符，但缩写的字符分类（\d、\w、\s 等）太宽泛。
# 你可以用方括号定义自己的字符分类。例如，字符分类[aeiouAEIOU]将匹
# 配所有元音字符，不论大小写。
import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

# 也可以使用短横表示字母或数字的范围。
# 例如，字符分类[a-zA-Z0-9]将匹配所 有小写字母、大写字母和数字。
# 请注意，在方括号内，普通的正则表达式符号不会被解释。这意味着，
# 你不需要前面加上倒斜杠转义.、*、?或()字符。例如，字符分类将匹
# 配数字 0 到 5 和一个 句点。你不需要将它写成[0-5\.]。

# 通过在字符分类的左方括号后加上一个插入字符（^），就可以得到“非字符类”。
# 非字符类将匹配不在这个字符类中的所有字符。类似去反
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')