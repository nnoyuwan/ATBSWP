# 利用内建的 subprocess 模块中的 Popen()函数， Python 程序可以启动计算机中的
# 其他程序（ Popen()函数名中的 P 表示 process，进程）。如果你打开了一个应用程序
# 的多个实例，每个实例都是同一个程序的不同进程。例如，如果你同时打开了 Web
# 浏览器的多个窗口，每个窗口都是 Web 浏览器程序的不同进程。

# 每个进程可以有多个线程。不像线程，进程无法直接读写另一个进程的变量。
# 如果你认为多线程程序是多个手指在追踪源代码，那么同一个程序打开多个进程就像
# 有一个朋友拿着程序源代码的独立副本。你们都独立地执行相同的程序。

import subprocess

# popen = subprocess.Popen('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')
# <subprocess.Popen object at 0x00000000034B4BE0>

# 返回值是一个 Popen 对象，它有两个有用的方法： poll()和 wait()。

# 可以认为 poll()方法是问你的朋友，她是否执行完毕你给她的代码。如果这个
# 进程在 poll()调用时仍在运行， poll()方法就返回 None。如果该程序已经终止，
# 它会返回该进程的整数退出代码。退出代码用于说明进程是无错终止（退出代码
# 为 0），还是一个错误导致进程终止（退出代码非零，通常为 1，但可能根据程序
# 而不同）。

# wait()方法就像是等着你的朋友执行完她的代码，然后你继续执行你的代码。
# wait()方法将阻塞，直到启动的进程终止。如果你希望你的程序暂停，直到用户完成
# 与其他程序，这非常有用。 wait()的返回值是进程的整数退出代码。
popen = subprocess.Popen('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')
print(popen.poll() == None)

popen.wait()

popen.poll()

# 15.8.1 向 Popen()传递命令行参数
# 用 Popen()创建进程时，可以向进程传递命令行参数。要做到这一点，向 Popen()
# 传递一个列表，作为唯一的参数。该列表中的第一个字符串是要启动的程序的可执
# 行文件名，所有后续的字符串将是该程序启动时，传递给该程序的命令行参数。实
# 际上，这个列表将作为被启动程序的 sys.argv 的值。

# 大多数具有图形用户界面（ GUI）的应用程序，不像基于命令行或基于终端的
# 程序那样尽可能地使用命令行参数。但大多数 GUI 应用程序将接受一个参数， 表示
# 应用程序启动时立即打开的文件。例如，如果你使用的是 Windows，创建一个简单
# 的文本文件 C:\hello.txt，然后在交互式环境中输入以下代码：

# subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
subprocess.Popen(["D:\\Program Files\\JetBrains\\PyCharm 2021.1.3\\bin\\pycharm64.exe",
                  'C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第15章 保持时间、计划任务和启动程序\\1.time模块.py'])

# 15.8.2 Task Scheduler、 launchd 和 cron

# 如果你精通计算机，可能知道 Windows 上的 Task Scheduler， OS X 上的
# launchd，或 Linux 上的 cron 调度程序。这些工具文档齐全，而且可靠，它们都允许
# 你安排应用程序在特定的时间启动。如果想更多地了解它们，可以在 http://nostarch.
# com/automatestuff/找到教程的链接。
# 利用操作系统内置的调度程序，你不必自己写时钟检查代码来安排你的程序。但
# 是，如果只需要程序稍作停顿，就用 time.sleep()函数。或者不使用操作系统的调度程
# 序，代码可以循环直到特定的日期和时间，每次循环时调用 time.sleep(1)

# 15.8.3 用 Python 打开网站

# webbrowser.open()函数可以从程序启动 Web 浏览器，打开指定的网站，而不是
# 用 subprocess.Popen()打开浏览器应用程序。详细内容参见第 11 章的“项目：利用
# webbrowser 模块的 mapIt.py”一节。

# 15.8.4 运行其他 Python 脚本
# subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])


# 15.8.5 用默认的应用程序打开文件

# 每个操作系统都有一个程序，其行为等价于双击文档文件来打开它。在 Windows
# 上，这是 start 程序。

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')

fileObj.close()
import subprocess

subprocess.Popen(['start', 'hello.txt'], shell=True)

# 这里，我们将 Hello world!写入一个新的 hello.txt 文件。然后调用 Popen()，传入一个
# 列表，其中包含程序名称（在这个例子中，是 Windows 上的'start'），以及文件名。 我们也
# 传入了 shell=True 关键字参数，这只在 Windows 上需要。操作系统知道所有的文件关联，
# 能弄清楚应该启动哪个程序，比如 Notepad.exe，来处理 hello.txt 文件。

# 在 OS X 上， open 程序用于打开文档文件和程序。如果你有 Mac，在交互式环
# 境中输入以下代码：
# >>> subprocess.Popen(['open', '/Applications/Calculator.app/'])
# <subprocess.Popen object at 0x10202ff98>
