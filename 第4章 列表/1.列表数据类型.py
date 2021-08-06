# 4.1.1 用下标取得列表中的单个值
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])

spam1 = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam1[0])
print(spam1[1][3])  # 多重下标,第一个下标表明使用哪个列表值，第二个下标表明该列表值中的值

# 4.1.2 负数下标
print(spam[-1])
print(spam[-3])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

# 4.1.3 利用切片取得子列表
print(spam[1:3])  # 1~2,不包括3
# 作为快捷方法， 你可以省略切片中冒号两边的一个下标或两个下标。省略第一
# 个下标相当于使用 0， 或列表的开始。省略第二个下标相当于使用列表的长度， 意
# 味着分片直至列表的末尾。在交互式环境中输入以下代码：
print('*' * 10)
print(spam[:2])  # 0 1
print(spam[1:])  # 1 2 3
print(spam[:])  # 0 1 2 3

# 4.1.4 用 len()取得列表的长度
len(spam)

# 4.1.5 用下标改变列表中的值
spam[1] = 'aardvark'
spam

spam[2] = spam[1]
spam

spam[-1] = 12345
spam

# 4.1.6 列表连接和列表复制
[1, 2, 3] + ["A", "B", "C"]

["X", "Y", "Z"] * 3

spam = [1, 2, 3]
spam += ["A", "B", "C"]
spam

# 4.1.7 用 del 语句从列表中删除值
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
del spam[2]
spam
