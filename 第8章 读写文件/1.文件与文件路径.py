# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/14 2:00 下午

# 当程序运行时， 变量是保存数据的好方法， 但如果希序结束后数据仍然保持， 就需要将数据保存到文件中。 
# 你可以认为文件容是一个字字符串值，大小可能有几个GB。

# 补：[\u4e00-\u9fa5]匹配中文

# 根文件夹名为 C:\，也称为 C：盘。在 OS X 和 Linux 中，根文件夹是/。
# 在本书中， 我使用 Windows 风格的根文件夹，C:\。

#  附加卷，诸如 DVD 驱动器或 USB 闪存驱动器，在不同的操作系统上显示也不 同。
#  在 Windows 上，它们表示为新的、带字符的根驱动器。诸如 D:\或 E:\。
#  在 OS X 上，它们表示为新的文件夹，在/Volumes 文件夹下。
#  在 Linux 上，它们表
#  示为新的文件夹，在/mnt（"mount"）文件夹下。
#  同时也要注意，虽然文件夹名称和文件名在 Windows 和 OS X 上是不区分大小写的，但在 Linux 上是区分大小写

# 8.1.1 Windows 上的倒斜杠以及 OS X 和 Linux 上的正斜杠
# \:在 Windows 上，路径书写使用倒斜杠作为文件夹之间的分隔符。
# /:但在 OS X 和 Linux 上，使用正斜杠作为它们的路径分隔符 如/Users/yuwanmo/.sogouinput
import os

os.path.join('usr', 'bin', 'spam')  # OS X---Out[3]: 'usr/bin/spam'
# 我在 Windows 上运行这些交互式环境的例子，所以，os.path .join('usr', 'bin', 'spam')返回'usr\\bin\\spam'
# （请注意，倒斜杠有两个，因为每个倒斜杠需要由另一个 倒斜杠字符来转义）。

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

# C:\Users\asweigart/accounts.txt
# C:\Users\asweigart/details.csv
# C:\Users\asweigart/invite.docx

# 8.1.2 当前工作目录
# 利用 os.getcwd()函数， 可以取得当前工作路径的字符串
os.getcwd()  # Out[5]: '/Users/yuwanmo/PycharmProjects/ATBSWP'
# 可以利用 os.chdir()改变它。
os.chdir('/Users/yuwanmo/PycharmProjects/SVM')
os.getcwd()
# 如果要更改的当前工作目录不存在，Python 就会显示一个错误。
os.chdir('C:\\Windows\\System32')
os.chdir('/Users/yuwanmo/PycharmProjects/ATBSWP')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Windows\\System32'


# 8.1.3 绝对路径与相对路径
# 有两种方法指定一个文件路径。
# • “绝对路径”，总是从根文件夹开始。
# • “相对路径”，它相对于程序的当前工作目录。

# .  单个的句点（“点”）用作文件夹目名称时，是“这个目录”的缩 写。
# .. 两个句点（“点点”）意思是父文件夹。

# ![](https://moyuwan-image.oss-cn-hangzhou.aliyuncs.com/img/20210814162243.png)
# 相对路径开始处的.\是可选的。例如，.\spam.txt 和 spam.txt 指的是同一个文件。


# 8.1.4 用 os.makedirs()创建新文件夹
# 程序可以用 os.makedirs()函数创建新文件夹（目录）。在交互式环境中输入以下代码：
# >>> import os
#
# >>> os.makedirs('C:\\delicious\\walnut\\waffles')
#
# 这不仅将创建 C:\delicious 文件夹，也会在 C:\delicious 下创建 walnut 文件夹，
# 并在 C:\delicious\walnut 中创建 waffles 文件夹。也就是说，os.makedirs()将创建
# 所有必要的中间文件夹，目的是确保完整路径名存在。图 8-3 展示了这个文件夹的层次结构。

os.makedirs('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/你还好吗')

# 8.1.5 os.path 模块

# os.path 模块包含了许多与文件名和文件路径相关的有用函数。例如，你已经使用了
# os.path.join()来构建所有操作系统上都有效的路径。因为 os.path 是 os 模块中的
# 模块，所以只要执行 import os 就可以导入它。


# 8.1.6 处理绝对路径和相对路径
# 1.调用 os.path.abspath(path)将返回参数的绝对路径的字符串。这是将相对路径转 换为绝对路径的简便方法。
# 2.调用 os.path.isabs(path)，如果参数是一个绝对路径，就返回 True，如果参数是一个相对路径，就返回 False。
# 3.调用 os.path.relpath(path, start)将返回从 start 路径到 path 的相对路径的字符串。 如果没有提供 start，
# 就使用当前工作目录作为开始路径。

# 在交互式环境中，输入以下对 os.path.abspath()的调用：
os.path.abspath('.')
os.path.abspath('./第8章 读写文件/你还好吗')  # Out[18]: '/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/你还好吗'
os.path.isabs('.')
os.path.isabs(os.path.abspath('.'))

# 在交互式环境中，输入以下对 os.path.relpath()的调用：
os.path.relpath('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/1.文件与文件路径.py',
                '/Users/yuwanmo/PycharmProjects/ATBSWP')  # Out[4]: '第8章 读写文件/1.文件与文件路径.py'

os.path.relpath('/Users/yuwanmo/PycharmProjects/ATBSWP/第7章 模式匹配与正则表达式/15.项目：电话号码和 E-mail 地址提取程序.py',
                '/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/')  # 第7章 模式匹配与正则表达式/15.项目：电话号码和 E-mail 地址提取程序.py

# 调用 os.path.dirname(path)将返回一个字符串，它包含 path 参数中最后一个斜杠之前的所有内容。(所在文件夹绝对路径)
# 调用 os.path.basename(path)将返回一个字符串，它包含 path 参数 中最后一个斜杠之后的所有内容。（文件名）
# ![](https://moyuwan-image.oss-cn-hangzhou.aliyuncs.com/img/20210814171701.png)
path = '/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/1.文件与文件路径.py'
os.path.basename(path)
os.path.dirname(path)

# 如果同时需要一个路径的目录名称和基本名称，就可以调用 os.path.split()，获 得这两个字符串的元组
os.path.split(path)  # Out[18]: ('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件', '1.文件与文件路径.py')

# 同时也请注意，os.path.split()不会接受一个文件路径并返回每个文件夹的字符串的列表。如果需要这样，
# 请使用split()字符串方法，并根据 os.path.sep 中的字符串进行分割。
path.split(os.path.sep)
# 在 OS X 和 Linux 系统上，返回的列表头上有一个空字符串：
# ['',
#  'Users',
#  'yuwanmo',
#  'PycharmProjects',
#  'ATBSWP',
#  '第8章 读写文件',
#  '1.文件与文件路径.py']

# 8.1.7 查看文件大小和文件夹内容
# 一旦有办法处理文件路径，就可以开始搜集特定文件和文件夹的信息。os.path 模 块提供了一些函数，
# 用于查看文件的字节数以及给定文件夹中的文件和子文件夹。
# • 调用 os.path.getsize(path)将返回 path 参数中文件的字节数。
# • 调用 os.path.getsize(path)将返回 path 参数中文件的字节数。
# • 调用 os.listdir(path)将返回 文件和文件夹 字符串的列表，包含 path 参数中的每个文件
# （请注意，这个函数在 os 模块中，而不是 os.path）。

os.path.getsize('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/1.文件与文件路径.py')  # Out[20]: 7141B
os.listdir('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件')

# 如果想知道这个目录下所有文件的总字节数，就可以同时 使用 os.path.getsize()和 os.listdir()。

totalSize = 0
for filename in os.listdir('第7章 模式匹配与正则表达式'):
    totalSize += totalSize + os.path.getsize(os.path.join('第7章 模式匹配与正则表达式', filename))
print(totalSize)  # 244276378 Byte

# 8.1.8 检查路径有效性
# 如果你提供的路径不存在，许多 Python 函数就会崩溃并报错。os.path 模块提 供了一些函数，
# 用于检测给定的路径是否存在，以及它是文件还是文件夹。
# • 如果 path 参数所指的文件或文件夹存在，调用 os.path.exists(path)将返回 True， 否则返回 False。
#
# • 如果 path 参数存在，并且是一个文件，调用 os.path.isfile(path)将返回 True，否 则返回 False。
#
# • 如果 path 参数存在，并且是一个文件夹，调用 os.path.isdir(path)将返回 True， 否则返回 False。 下面是我在交互式环境中尝试这些函数的结果：

os.path.exists('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件')  # True
os.path.exists('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/123')  # # False
os.path.isdir('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件')  # True
os.path.isfile('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件')  # False
os.path.isdir('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/1.文件与文件路径.py')  # False
os.path.isfile('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/1.文件与文件路径.py')  # True

# 利用 os.path.exists()函数，可以确定 DVD 或闪存盘当前是否连在计算机上。
# 例如，如果在 Windows 计算机上，我想用卷名 D:\检查一个闪存盘，可以这样做：
#
# >>> os.path.exists('D:\\') False
