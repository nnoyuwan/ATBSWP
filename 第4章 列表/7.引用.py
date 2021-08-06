# 当稍后将 spam 中的值改变为 100 时，
# 这不会影响 cheese 中的值。这是因为
# spam 和 cheese是不同的变量， 保存了不同的值。
spam = 42
cheese = spam
spam = 100
cheese

# 但列表不是这样的。 当你将列表赋给一个变量时，
# 实际上是将列表的“引用”赋给了该变量。引用是一
# 个值，指向某些数据。
spam = [0, 1, 2, 3, 4, 5]  # 列表变量实际上没有包含列表，而是包含了对列表的“引用”
cheese = spam  # 只是将 spam 中的列表引用拷贝到 cheese，而不是列表值本身。
cheese[1] = 'hello'
# 指向了同一个列表。底下只有一个列表，
# 因为列表本身实际从未复制。所以当
# 你修改 cheese 变量的第一个元素时，
# 也修改了 spam 指向的同一个列表。
spam
cheese  # 当你改变 cheese 指向的列表时， spam 指向的列表也发生了改变

# 在变量必须保存可变数据类型的值时， 例如列表或字典，Python 就使用引用。
# 对于不可变的数据类型的值， 例如字符串、 整型或元组， Python变量就保存值本身。


# 4.7.2 copy 模块的 copy()和 deepcopy()函数
# 如果函数修改了
# 传入的列表或字典， 你可能不希望这些变动影响原来的列表或字典。要做到这一点，
# Python 提供了名为 copy 的模块， 其中包含 copy()和 deepcopy()函数

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)  # 现在 spam 和 cheese 变量指向两个独立的列表['A', 'B', 'C', 'D']
cheese[1] = 42
spam  # ['A', 'B', 'C', 'D']
cheese  # ['A', 42, 'C', 'D']
# deepcopy()函数将同时复制它们内部的列表(引用类型)。




