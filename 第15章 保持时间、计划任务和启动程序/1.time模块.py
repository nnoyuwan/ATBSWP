# 坐在电脑前运行程序是不错的，但在你没有直接监督时运
# 行程序，也是有用的。计算机的时钟可以调度程序，在特定的
# 时间和日期运行，或定期运行。例如，程序可以每小时抓取一
# 个网站，检查变更，或在凌晨 4 点你睡觉时，执行 CPU 密集
# 型任务。 Python 的 time 和 datetime 模块提供了这些函数。
# 利用 subprocess 和 threading 模块，你也可以编程按时启动
# 其他程序。通常，编程最快的方法是利用其他人已经写好的应
# 用程序。

# 15.1 time 模块
# 计算机的系统时钟设置为特定的日期、时间和时区。内置的 time 模块让 Python
# 程序能读取系统时钟的当前时间。在 time 模块中， time.time()和 time.sleep()函数是
# 最有用的模块。

# 15.1.1 time.time()函数
# Unix 纪元是编程中经常参考的时间： 1970 年 1 月 1 日 0 点，即协调世界时
# （ UTC）。 time.time()函数返回自那一刻以来的秒数，是一个浮点值（回想一下，浮
# 点值只是一个带小数点的数）。这个数字称为 UNIX 纪元时间戳。例如，在交互式
# 环境中输入以下代码：

import time

time.time()  # 浮点数 1630033555.1123457


# 如果在代码块开始时调用 time.time()， 并在结束时再次调用，就可以
# 用第二个时间戳减去第一个，得到这两次调用之间经过的时间。


def calProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


# startTime = time.time()
# prod = calProd()
# endTime = time.time()
# print('The result is %s digits long.' % len(str(prod)))
# print('Took %s seconds to calculate.' % (endTime - startTime))
#
# import cProfile
# import re
#
# cProfile.run('calProd()')

# 15.1.2 time.sleep()函数
# 如果需要让程序暂停一下，就调用 time.sleep()函数，并传入希望程序暂停的秒数。

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

time.sleep(5)

# for 循环将打印 Tick，暂停一秒钟，打印 Tock，暂停一秒钟，打印 Tick，
# 暂停，如此继续，直到 Tick 和 Tock 分别被打印 3 次。
# time.sleep()函数将阻塞（也就是说，它不会返回或让程序执行其他代码），直到
# 传递给 time.sleep()的秒数流逝。例如，如果输入 time.sleep(5) ，会在 5 秒后才看
# 到下一个提示符（ >>>）。
# 请注意，在 IDLE 中按 Ctrl-C 不会中断 time.sleep()调用。 IDLE 会等待到暂停结
# 束，再抛出 KeyboardInterrupt 异常。要绕过这个问题，不要用一次 time.sleep(30)调
# 用来暂停 30 秒，而是使用 for 循环执行 30 次 time.sleep(1)调用。

# for i in range(30):
#     time.sleep(1)

