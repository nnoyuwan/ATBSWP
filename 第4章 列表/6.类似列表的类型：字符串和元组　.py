# 列表并不是唯一表示序列值的数据类型。例如， 字符串和列表实际上很相似，
# 只要你认为字符串是单个文本字符的列表。

name = 'Zophie'
name[0]
name[-2]
name[0:4]

'Zo' in name
'z' in name
'p' not in name

for i in name:
    print(' * ' * 3 + i + " * " * 3)

# 4.6.1 可变和不可变数据类型

# 列表是“ 可变的” 数据类型，它
# 的值可以添加、 删除或改变。但是， 字符串是“不可变的”， 它不能被更改
name = 'Zophie a cat'
name[7] = 'the'  # TypeError: 'str' object does not support item assignment

# “改变” 一个字符串的正确方式， 是使用切片和连接。构造一个“ 新的” 字符
# 串， 从老的字符串那里复制一些部分。
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
newName

eggs = [1, 2, 3]
eggs = [4, 5, 6]
eggs  # 这里 eggs 中的列表值并没有改变， 而是整个新的不同的列表值([4, 5, 6])，覆写了老的列表值。

# 如果你确实希望修改 eggs 中原来的列表， 让它包含[4, 5, 6]， 就要这样做：
eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
eggs

# 4.6.2 元组数据类型--元组数据类型，它是列表数据类型的不可变形式。
# 元组输入时用圆括号()， 而不是用方括号[]
eggs = ("hello", 42, 0.5)
eggs[0]
eggs[1:3] // (42, 0.5)
len(eggs)

# 元组像字符串一样， 是不可变的
eggs[0] = "world"  # TypeError: 'tuple' object does not support item assignment

# 如果元组中只有一个值， 你可以在括号内该值的后面跟上一个逗号，
# 表明这种情况。 否则， Python 将认为， 你只是在一个普通括号
# 内输入了一个值。逗号告诉Python， 这是一个元组
type(("hello",))  # <class 'tuple'>
type(("hello"))  # <class 'str'>

# 4.6.3 用 list()和 tuple()函数来转换类型
# 函数 list()和 tuple()将返回传递给它们的值的列表和元组版本
tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello')