# 假定你希望对某个文件夹中的所有文件改名， 包括该文件夹中所有子文件夹中
# 的所有文件。也就是说， 你希望遍历目录树， 处理遇到的每个文件。写程序完成这
# 件事，可能需要一些技巧。 好在， Python 提供了一个函数， 替你处理这个过程。

import os

for floderName, subfloders, filenames in os.walk('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第9章 组织文件'):
    print('The current floder is ' + floderName)
    for subfloder in subfloders:
        print('SUBFLODER OF ' + floderName + ": " + subfloder)
    for filename in filenames:
        print('FILE INSIDE ' + floderName + ": " + filename)
    print('')

# os.walk()函数被传入一个字符串值，即一个文件夹的路径。你可以在一个 for
# 循环语句中使用 os.walk()函数，遍历目录树， 就像使用 range()函数遍历一个范围的
# 数字一样。不像 range()， os.walk()在循环的每次迭代中，返回 3 个值：
# 1． 当前文件夹名称的字符串。
# 2． 当前文件夹中子文件夹的字符串的列表。
# 3． 当前文件夹中文件的字符串的列表。

# 运行该程序， 它的输出如下：

# The current floder is C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件
# SUBFLODER OF C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件: dest
# SUBFLODER OF C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件: dest2
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件: 1.shutil 模块.py
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件: 2.遍历目录树.py

# The current floder is C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest: Python编程快速上手  让繁琐工作自动化.pdf
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest: spam.rxt
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest: spam.txt
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest: spam1.txt
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest: 陀飞轮-陈奕迅.flac
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest: 陀飞轮-陈奕迅.mp3

# The current floder is C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest2
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest2: spam.txt
# FILE INSIDE C:\Users\admin\PycharmProjects\ATBSWP\第9章 组织文件\dest2: spam1.txt
