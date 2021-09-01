# 为了引入多线程的概念，让我们来看一个例子。假设你想安排一些代码，在一
# 段延迟后或在特定时间运行。可以在程序启动时添加如下代码

import time, datetime

startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)

while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Halloween 2029')

# 这段代码指定 2029 年 10 月 31 日作为开始时间，不断调用 time.sleep(1)，直到开
# 始时间。在等待 time.sleep()的循环调用完成时，程序不能做任何事情，它只是坐在那
# 里，直到 2029 年万圣节。这是因为 Python 程序在默认情况下，只有一个执行线程。


# 15.6.1 向线程的目标函数传递参数
print('Cats', 'Dogs', 'Frogs', sep=' & ')

import threading

# 该 print()调用有 3 个常规参数： 'Cats'、 'Dogs'和'Frogs'，以及一个关键字参数： sep=
# ' & '。常规参数可以作为一个列表，传递给 threading.Thread()中的 args 关键字参数。关
# 键字参数可以作为一个字典，传递给 threading.Thread()中的 kwargs 关键字参数。

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()

# 下面创建新线程调用 print()的方法是不正确的：
# threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))

# 这行代码最终会调用 print()函数，将它的返回值（ print()的返回值总是无）作为
# target 关键字参数。它没有传递 print()函数本身。如果要向新线程中的函数传递参数，
# 就使用 threading.Thread()函数的 args 和 kwargs 关键字参数。

# 15.6.2 并发问题
# 可以轻松地创建多个新线程，让它们同时运行。但多线程也可能会导致所谓的
# 并发问题。如果这些线程同时读写变量，导致互相干扰，就会发生并发问题。并发
# 问题可能很难一致地重现，所以难以调试。
# 多线程编程本身就是一个广泛的主题，超出了本书的范围。必须记住的是：为了避
# 免并发问题，绝不让多个线程读取或写入相同的变量。当创建一个新的
# Thread
# 对象时，
# 要确保其目标函数只使用该函数中的局部变量。这将避免程序中难以调试的并发问题。
