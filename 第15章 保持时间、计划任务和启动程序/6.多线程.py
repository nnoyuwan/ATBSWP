# 为了引入多线程的概念，让我们来看一个例子。假设你想安排一些代码，在一
# 段延迟后或在特定时间运行。可以在程序启动时添加如下代码

import time, datetime

startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)

while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Halloween 2029')
