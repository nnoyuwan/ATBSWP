catNames = []
while True:
    print("Enter the name of cat " + str(len(catNames) + 1)
          + "(or enter nothing to stop.):")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]
print("The cat names are:")
for name in catNames:
    print(name)

# 4.2.1 列表用于循环
for i in range(4):
    print(i)

# 一个常见的 Python 技巧， 是在 for 循环中
# 使用 range(len(someList))， 迭代列表的每一个下标
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

# 4.2.2 in 和 not in 操作符
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
'howdy' not in ['hello', 'hi', 'howdy', 'heyas']

# 4.2.3 多重赋值技巧
cat = ["fat", "black", "loud"]
size, color, disposition = cat
