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


