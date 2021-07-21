for i in range(12, 16):
    print(i)

print('*' * 10)

for i in range(0, 10, 2):
    print(i)

print('*' * 10)
# 在为 for 循环生成序列数据方面， range()函数很灵活。举例来说，甚至可以用
# 负数作为步长参数，让循环计数逐渐减少，而不是增加。
for i in range(5, -1, -2):
    print(i)