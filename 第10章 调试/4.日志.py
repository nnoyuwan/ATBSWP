# 如果你曾经在代码中加入 print() 语句，在程序运行时输出某些变量的值，你
# 就使用了记日志的方式来调试代码。记日志是一种很好的方式，可以理解程序中
# 发生的事，以及事情发生的顺序。 Python 的 logging 模块使得你很容易创建自定义
# 的消息记录。这些日志消息将描述程序执行何时到达日志函数调用，并列出你指
# 定的任何变量当时的值。另一方面，缺失日志信息表明有一部分代码被跳过，从
# 未执行。

# 10.4.1 使用日志模块
# 要启用 logging 模块，在程序运行时将日志信息显示在屏幕上，请将下面的代
# 码复制到程序顶部（但在 Python 的#!行之下）：

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# 你不需要过于担心它的工作原理，但基本上，当 Python 记录一个事件的日志时，
# 它会创建一个 LogRecord 对象，保存关于该事件的信息。 logging 模块的函数让你
# 指定想看到的这个 LogRecord 对象的细节，以及希望的细节展示方式。

# 假如你编写了一个函数，计算一个数的阶乘。在数学上， 4 的阶乘是
# 1 × 2 × 3 × 4，即 24。 7 的阶乘是 1 × 2 × 3 × 4 × 5 × 6 × 7，即 5040。打开一个新的
# 文件编辑器窗口，输入以下代码。其中有一个缺陷，但你也会输入一些日志信息，
# 帮助你弄清楚哪里出了问题。将该程序保存为 factorialLog.py
logging.debug('Start of program')


def factorial(n):
    logging.debug('start of factorial(%s)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % n)
    return total


print(factorial(5))
logging.debug('End of program')

# # 2021-08-17 22:02:30,568 - DEBUG - Start of program
# #  2021-08-17 22:02:30,568 - DEBUG - start of factorial(5)
# #  2021-08-17 22:02:30,569 - DEBUG - i is 0, total is 0
# #  2021-08-17 22:02:30,569 - DEBUG - i is 1, total is 0
# #  2021-08-17 22:02:30,569 - DEBUG - i is 2, total is 0
# #  2021-08-17 22:02:30,569 - DEBUG - i is 3, total is 0
# #  2021-08-17 22:02:30,569 - DEBUG - i is 4, total is 0
# #  2021-08-17 22:02:30,569 - DEBUG - i is 5, total is 0
# #  2021-08-17 22:02:30,569 - DEBUG - End of factorial(5)
# #  2021-08-17 22:02:30,569 - DEBUG - End of program

# factorial() 函数返回 0 作为 5 的阶乘，这是不对的。 for 循环应该用从 1 到 5
# 的数，乘以 total 的值。但 logging.debug() 显示的日志信息表明， i 变量从 0 开始，
# 而不是 1。因为 0 乘任何数都是 0，所以接下来的迭代中， total 的值都是错的。日志消息提供了可以追踪的痕迹，帮助你弄清楚何时事情开始不对。
# 将代码行 for i in range（ n + 1）：改为 for i in range（ 1， n + 1）：，再次运行程序。
# 输出看起来像这样：

#  2021-08-17 22:04:41,317 - DEBUG - Start of program
#  2021-08-17 22:04:41,317 - DEBUG - start of factorial(5)
#  2021-08-17 22:04:41,317 - DEBUG - i is 1, total is 1
#  2021-08-17 22:04:41,317 - DEBUG - i is 2, total is 2
#  2021-08-17 22:04:41,317 - DEBUG - i is 3, total is 6
#  2021-08-17 22:04:41,318 - DEBUG - i is 4, total is 24
#  2021-08-17 22:04:41,318 - DEBUG - i is 5, total is 120
#  2021-08-17 22:04:41,318 - DEBUG - End of factorial(5)
#  2021-08-17 22:04:41,318 - DEBUG - End of program
