if __name__ == '__main__':
    # # 1.1 在交互式环境中输入表达式　
    # print(2 ** 8)
    # print(23 // 7)  # 整除 23 / 7 = 3 …… 2 取3
    #
    # # 1.3 字符串连接和复制
    # print('Alice' + 'Bob')
    # print('Alice ' * 5)
    # # pt('Alice ' * 5.0) # TypeError: can't multiply sequence by non-int of type 'float'
    #
    # # 1.5 第一个程序
    # print('hello world!')
    # print('what\'s your name?')
    # myName = input()
    # print('It\'s nice to meet you,' + myName)
    #
    # print('The length of your name is:' + str(len(myName)))
    #
    # print('what\'s your age?')
    # myAge = input()
    # print('you\'ll be ' + str(int(myAge) + 1) + ' in a year.')

    # # 1.6.6 str()、 int()和 float()函数
    # print(str(0))
    # print(str(-3.14))
    # print(int('42'))
    # print(int('-99'))
    # print(int(1.25))
    # print(int(1.99))
    # print(float('3.14'))
    # print(float(10))

    # input()函数总是返回一个字符串， 即便用户输入的是一个数字
    spam = input() # input 101
    print(type(spam)) # <class 'str'>
