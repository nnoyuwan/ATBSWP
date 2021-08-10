# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/9 4:59 下午

# 6.2.1 字符串方法 upper()、lower()、isupper()和 islower()
spam = 'Hello, World!'
upper = spam.upper()
print(upper)
print(id(upper), id(spam))
lower = spam.lower()

# 请注意，这些方法没有改变字符串本身，而是返回一个新字符串。如果
# 你希望改 变原来的字符串，就必须在该字符串上调用 upper()或 lower()，
# 然后将这个新字符串 赋给保存原来字符串的变量。

# 请注意，这些方法没有改变字符串本身，而是返回一个新字符串。如果
# 你希望改 变原来的字符串，就必须在该字符串上调用 upper()或 lo
# wer()，然后将这个新字符串 赋给保存原来字符串的变量。
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# 如果字符串至少有一个字母，并且所有字母都是大写或小写，
# isupper()和islower()方法就会相应地返回布尔值 True。
# 否则，该方法返回 False。

spam = 'Hello World!'
spam.islower()
spam.isupper()
'HELLO'.islower()
'abc1234'.islower()
'12345'.islower()
'12345'.isupper()

# 因为 upper()和 lower()字符串方法本身返回字符串，所以
# 也可以在“那些”返回 的字符串上继续调用字符串方法。这样做
# 的表达式看起来就像方法调用链。在交互 式环境中输入以下代码：
'Hello'.upper()
'Hello'.upper().lower()
'Hello'.upper().lower().upper()
'HELLO'.lower()
'HELLO'.lower().islower()

# 6.2.2 isX 字符串方法
# isalpha()返回 True，如果字符串只包含字母，并且非空
# isalnum()返回 True，如果字符串只包含字母和数字，并且非空；
# isdecimal()返回 True，如果字符串只包含数字字符，并且非空；
# isspace()返回 True，如果字符串只包含空格、制表符和换行，并且非空；
# istitle()返回 True，如果字符串仅包含以大写字母开头、后面都是小写字母的单词。
# 在交互式环境中输入以下代码：

'hello'.isalpha()
'hello123'.isalpha()
'hello123'.isalnum()
'hello'.isalnum()
'123'.isdecimal()
' '.isspace()
'This Is Title Case'.istitle()
'This Is Title Case 123'.istitle()
'This Is not Title Case'.istitle()
'This Is NOT Title Case Either'.istitle()

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and number.')

# 6.2.3 字符串方法 startswith()和 endswith()
'Hello world!'.startswith('Hello')
'Hello world!'.endswith('world!')
'abc123'.startswith('abcdef')
'abc123'.endswith('12')
'Hello world!'.startswith('Hello world!')
'Hello world!'.endswith('Hello world!')

# 6.2.4 字符串方法 join()和 split()
# 调用 join()方法的字符串，被插入到列表参数中每个字符串的中间。
','.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Simon'])
'ABC'.join(['My', 'name', 'is', 'Simon'])

# 调用 join()方法的字符串，被插入到列表参数中每个字符串的中间
'My name is Simon'.split()
'My name is Simon'.split(' ')
'My name is Simon'.split('m')
'MyABCnameABCisABCSimon'.split('ABC')

spam = '''Dear Alice
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely, 
Bob'''

spam.split('\n')

# 6.2.5 用 rjust()、ljust()和center()方法对齐文本
'Hello'.rjust(10)
'Hello'.rjust(20)
'Hello World'.rjust(20)
'Hello'.ljust(10)

# rjust()和 ljust()方法的第二个可选参数将
# 指定一个填充字符，取代空格字符。
'Hello'.rjust(10, '*')
'Hello'.ljust(10, '-')

# center()字符串方法与 ljust()与 rjust()类似，
# 但它让文本居中，而不是左对齐或右对齐。
'Hello'.center(20)
'Hello'.center(20, '=')
