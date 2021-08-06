# 4.4.1 用 index()方法在列表中查找值
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hi')

# 如果列表中存在重复的值， 就返回它第一次出现的下标。
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')

# 4.4.2 用 append()和 insert()方法在列表中添加值
# append()添加在末尾，insert()添加到任何位置
# append()和 insert()方法是列表方法， 只能在列表上调用， 不能在其他值上调用，
spam = ['cat', 'dog', 'bat']
spam.append('mouse')
spam

spam.insert(1, ' chicken')
spam

# 4.4.3 用 remove()方法从列表中删除值
# 知道下标用del
# 知道值用remove

# 如果该值在列表中出现多次， 只有第一次出现的值会被删除
# 删除列表中不存在的值， 将导致 ValueError 错误
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('cat')
spam

# 4.4.4 用 sort()方法将列表中的值排序
# spam = [2, 5, 3.14, 1, -7]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
# spam.sort()
spam.sort(reverse=True)
spam

# 不能对既有数字又有字符串值的列表排序，
# 因为 Python 不知道如何比较它们。
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

# sort()方法对字符串排序时， 使用“ ASCII 字符顺序”， 而不是实际的字
# 典顺序
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam

# 如果需要按照普通的字典顺序来排序， 就在 sort()方法调用时，
# 将关键字参数key 设置为 str.lower。
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam

# Python 中缩进规则的例外
# 1.列表实际上可以跨越几行。这些行
# 的缩进并不重要。 Python 知道， 没有看到结束方括号， 列表就没有结束。
spam = ['apples',
                'oranges',
'bananas',
        'cats']
print(spam)
# 2.也可以在行末使用续行字符\， 将一条指令写成多行。可以把\看成是“ 这条
# 指令在下一行继续”。
print('Four score and seven ' + \
      'years ago...')
