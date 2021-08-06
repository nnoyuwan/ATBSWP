# 4.9 习题
# 2.
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
spam

spam = ['a', 'b', 'c', 'd']
# 3.
i = int('3' * 2)  # = int('33')
i  # 33
spam[int(i / 11)]

# 4.
spam[-1]

# 5.
spam[:2]

bacon = [3.14, 'cat', 11, 'cat', True]

# 6.
bacon.index('cat')

# 7.
bacon.append(99)
bacon

# 8.
bacon.remove('cat')  # 移除最末尾的'cat'
bacon

# 9. 连接:+;复制:copy

# 10. append在末尾追加；insert在任意位置插入

# 11. 删除1.remove(不知道index);2.del（指定index）

# 12.字符串类似char（字符）列表

# 13.元组是不能修改的列表

# 14.
spam = (42,)
spam = (42)
type(spam)

# 15.
spam = ()
spam = list(spam)
spam = tuple(spam)
type(spam)

# 16. 列表的引用
