birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I don\'t have birthday information for ' + name)
        print('What\'s their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')

# 5.1.2 keys()、 values()和 items()方法
spam = {'color': 'red', 'age': 42}
for k in spam.keys():
    print(k)

for v in spam.values():
    print(v)

for i in spam.items():
    print(i)

print(spam.keys())
print(spam.values())
print(spam.items())

# 如果希望通过这些方法得到一个真正的列表，
# 就把类似列表的返回值传递给 list函数。
list(spam.keys())

# 可以利用多重赋值的技巧，在 for 循环中将键和值赋给不同的变量。
for k, v in spam.items():
    print("key=" + k + ' ,value=' + str(v))

