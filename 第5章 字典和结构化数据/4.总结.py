# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/9 12:07 下午

# 不像列表，只包含一系列有序的值。字典中的值是
# 通过方括号访问的，像列表一样。字典不是只能使
# 用整数下标，而是可以用各种数据类型 作为键：整
# 型、浮点型、字符串或元组。

# 4．如果 spam 是{'bar': 100}，你试图访问 spam['foo']，会发生什么？
spam = {'bar': 100}
spam['foo']  # KeyError: 'foo'

# 5．如果一个字典保存在 spam 中，表达式'cat' in spam
# 和'cat' in spam.keys()之间 的区别是什么？
# ans:前者是后者的简写版本

# 6．如果一个字典保存在变量中，表达式'cat' in spam
# 和'cat' in spam.values()之间 的区别是什么？
# ans：前者为'cat' in spam.keys()的缩写，
# 一个是查是否在键中存在；一个查是否在值中存在

# 7．下面代码的简洁写法是什么？
if 'color' not in spam:
    spam['color'] = 'black'

# ans
spam.setdefault('color', 'black')

# 8
# pprint
