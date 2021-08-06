message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for c in message:
    count.setdefault(c, 0)
    count[c] = count[c] + 1
print(count)
# setdefault()
# 方法调用确保了键存在于 count 字典中（默认值是 0）
