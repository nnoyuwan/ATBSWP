import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for c in message:
    count.setdefault(c, 0)
    count[c] = count[c] + 1
print(count)
# setdefault()
# 方法调用确保了键存在于 count 字典中（默认值是 0）

pprint.pprint(count)
# 这一次， 当程序运行时， 输出看起来更干净，键排过序
