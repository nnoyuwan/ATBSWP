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


# 10.4.2 不要用 print()调试
# 输入 import logging 和 logging.basicConfig（ level=logging.DEBUG, format='%
# (asctime)s - %(levelname)s - %(message)s'）有一点不方便。你可能想使用 print() 调用
# 代替，但不要屈服于这种诱惑！在调试完成后，你需要花很多时间，从代码中清除每
# 条日志消息的 print() 调用。你甚至有可能不小心删除一些 print() 调用，而它们不是用
# 来产生日志消息的。日志消息的好处在于，你可以随心所欲地在程序中想加多少就加
# 多少，稍后只要加入一次 logging.disable（ logging.CRITICAL）调用，就可以禁止日
# 志。不像 print()， logging 模块使得显示和隐藏日志信息之间的切换变得很容易

# 日志消息是给程序员的，不是给用户的。用户不会因为你便于调试，而想看到
# 的字典值的内容。请将日志信息用于类似这样的目的。对于用户希望看到的消息，
# 例如“文件未找到”或者“无效的输入，请输入一个数字”，应该使用 print() 调用。
# 我们不希望禁用日志消息之后，让用户看不到有用的信息。


# 10.4.3 日志级别
# “日志级别”提供了一种方式，按重要性对日志消息进行分类。 5 个日志级别如表
# 10-1 所示，从最不重要到最重要。利用不同的日志函数，消息可以按某个级别记入日志。

# 级别        日志函数                    描述
# DEBUG      logging.debug()    最低级别。用于小细节。通常只有在诊断问题时，你才会关心这些消息
# INFO       logging.info()     用于记录程序中一般事件的信息，或确认一切工作正常
# WARNING    logging.warning()  用于表示可能的问题，它不会阻止程序的工作，但将来可能会
# ERROR      logging.error()    用于记录错误，它导致程序做某事失败
# CRITICAL   logging.critical() 最高级别。用于表示致命的错误，它导致或将要导致程序完全停止工作

# 日志消息作为一个字符串，传递给这些函数。日志级别是一种建议。归根到底，
# 还是由你来决定日志消息属于哪一种类型。在交互式环境中输入以下代码：

import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# 向 basicConfig()函数
# 传入 logging.DEBUG 作为 level 关键字参数，这将显示所有日志级别的消息（ DEBUG
# 是最低的级别）。但在开发了更多的程序后，你可能只对错误感兴趣。在这种情况
# 下，可以将 basicConfig() 的 level 参数设置为 logging.ERROR，这将只显示 ERROR
# 和 CRITICAL 消息，跳过 DEBUG、 INFO 和 WARNING 消息。

# 打印结果
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Some debugging details.')
# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# 2021-08-18 10:50:02,900 - ERROR - An error has occurred.
# logging.critical('The program is unable to recover!')
# 2021-08-18 10:50:03,370 - CRITICAL - The program is unable to recover!


# 10.4.4 禁用日志
# 在调试完程序后，你可能不希望所有这些日志消息出现在屏幕上。 logging.
# disable() 函数禁用了这些消息，这样就不必进入到程序中，手工删除所有的日志调
# 用。
#
# 只要向 logging.disable() 传入一个日志级别，它就会禁止该级别和更低级别的所
# 有日志消息。所以，如果想要禁用所有日志，只要在程序中添加 logging. disable
# （ logging.CRITICAL）。例如，在交互式环境中输入以下代码：

import logging

logging.disable(logging.INFO)

logging.debug('debug 信息')
logging.warning('只有这个会输出。。。')
logging.info('info 信息')

# 因为 logging.disable() 将禁用它之后的所有消息，你可能希望将它添加到程序中
# 接近 import logging 代码行的位置。这样就很容易找到它，根据需要注释掉它，或
# 取消注释，从而启用或禁用日志消息。

# 10.4.5 将日志记录到文件
# 除了将日志消息显示在屏幕上，还可以将它们写入文本文件。 logging.basic
# Config() 函数接受 filename 关键字参数，像这样：

import logging

logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 日志信息将被保存到 myProgramLog.txt 文件中。虽然日志消息很有用，但它们
# 可能塞满屏幕，让你很难读到程序的输出。将日志信息写入到文件，让屏幕保持干
# 净，又能保存信息，这样在运行程序后，可以阅读这些信息。可以用任何文件编辑
# 器打开这个文本文件，诸如 Notepad 或 TextEdit。


