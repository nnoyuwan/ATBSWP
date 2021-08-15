# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/11 11:58 下午

# 7.3.1 利用括号分组
# 假定想要将区号从电话号码中分离。添加括号将在正则表达式中创建“分组”：
# (\d\d\d)-(\d\d\d-\d\d\d\d)。然后可以使用 group()匹配对象方法，
# 从一个分组中获取匹 配的文本。
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group()  # '415-555-4242', 不传参数默认匹配整个对象

# 如果想要一次就获取所有的分组，请使用groups()方法，注意函数名的复数形式
mo.groups()  # ('415', '555-4242') 返回元组
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# 括号在正则表达式中有特殊的含义，但是如果你需要在文本中匹配括号，怎么办？
# 需要用倒斜杠对(和)进行字符转义
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.groups(1)
mo.groups(2)

# 7.3.2 用管道匹配多个分组
# 字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它。
# 例如， 正则表达式 r'Batman|Tina Fey'将匹配'Batman'或'Tina Fey'。
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
# 如果 Batman 和 Tina Fey 都出现在被查找的字符串中，
# 第一次出现的匹配文本， 将作为 Match 对象返回。
mo1.group()

heroRegex.findall('Batman and Tina Fey')  # ['Batman', 'Tina Fey'] 返回列表

# 也可以使用管道来匹配多个模式中的一个，作为正则表达式的一部分。
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
# 方法调用 mo.group()返回了完全匹配的文本'Batmobile'，
# 而mo.group(1)只是返回第一个括号分组内匹配的文本'mobile'。
# 通过使用管道字符和分组括号，可以指定 几种可选的模式，让正则表达式去匹配。
# 如果需要匹配真正的管道字符，就用倒斜杠转义，即\|。

# 7.3.3 用问号实现可选匹配
# 有时候，想匹配的模式是可选的。就是说，不论这段文本在不在，
# 正则表达式都会认为匹配。字符?表明它前面的分组在这个模式中是可选的。
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# 正则表达式中的(wo)?部分表明，模式wo是可选的分组。
# 该正则表达式匹配的文本中，wo 将出现零次或一次。


# 利用前面电话号码的例子，你可以让正则表达式寻找包含区号或不包含区号的电
# 话号码。在交互式环境中输入以下代码：
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  # (\d\d\d-)可有可无
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()  # 没有'415-'也可以匹配成功

# 7.3.4 用星号匹配零次或多次
# *（称为星号）意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出
# 现任意次。它可以完全不存在，或一次又一次地重复。

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()  # 对于'Batwowowowoman'，(wo)*匹配 wo 的 4 个实例。

# 7.3.5 用加号匹配一次或多次
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()  # AttributeError: 'NoneType' object has no attribute 'group'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()

mo2 = batRegex.search('The Adventures of Batman')
print(mo2 is None)  # 正则表达式 Bat(wo)+man 不会匹配字符串'The Adventures of Batman'，因为加号 要求 wo 至少出现一次。

# 7.3.6 用花括号匹配特定次数
# 如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括 号包围的数字。

# 1.例如，正则表达式(Ha){3}将匹配字符串'HaHaHa'，但不会匹配'HaHa'，
# 因为后者只重复了(Ha)分组两次。

# 2.除了一个数字，还可以指定一个范围，即在花括号中写下一个最小值、
# 一个逗号和一个最大值。例如，正则表达式(Ha){3,5}将匹配
# 'HaHaHa'、'HaHaHaHa'和'HaHaHaHaHa'。

# 3.也可以不写花括号中的第一个或第二个数字，不限定最小值或最大值。
# 例如，(Ha){3,}将匹配 3 次或更多次实例，(Ha){,5}将匹配 0 到 5 次实例。
# 花括号让正则表达式更简短。

# 这两个正则表达式匹配同样的模式：
re.compile(r'(Ha){3}')
re.compile(r'(Ha)(Ha)(Ha)')

# 这两个正则表达式也匹配同样的模式：
re.compile(r'(Ha){3,5}')
re.compile(r'((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))')

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

mo2 = haRegex.search('Ha')
print(mo2 is None)
