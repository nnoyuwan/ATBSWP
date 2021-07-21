def spam():
    # 如果需要在一个函数内修改全局变量， 就使用 global 语句
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
