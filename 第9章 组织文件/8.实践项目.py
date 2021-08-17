# 9.8.1 选择性拷贝
# 编写一个程序， 遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。
# 不论这些文件的位置在哪里， 将它们拷贝到一个新的文件夹中。
import os
import re
import shutil

print('请输入文件扩展名：')
ext = input()

print('请输入查找文件夹路径：')
floder = input()

p = re.compile(ext)
re_compile = p
dest = 'C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第9章 组织文件\\选择性拷贝'
for flodername, subfloders, filenames in os.walk(floder):
    for filename in filenames:
        if p.search(filename) is not None:
            shutil.move(os.path.join(flodername, filename),
                        os.path.join(dest, filename))

# 9.8.2 删除不需要的文件
# 一些不需要的、 巨大的文件或文件夹占据了硬盘的空间， 这并不少见。如果你
# 试图释放计算机上的空间， 那么删除不想要的巨大文件效果最好。但首先你必须找
# 到它们。
# 编写一个程序， 遍历一个目录树， 查找特别大的文件或文件夹， 比方说， 超过
# 100MB 的文件 （ 回忆一下，要获得文件的大小，可以使用 os 模块的 os.path.getsize()）。
# 将这些文件的绝对路径打印到屏幕上。
print('请输入文件夹路径：')
floder = input()

for flodername, subfloders, filenames in os.walk(floder):
    for filename in filenames:
        filesize = os.path.getsize(os.path.join(flodername, filename)) / 1024 / 1024
        if filesize > 100:
            print(filename + ': '
                  + str(filesize) + "MB")

# 9.8.3 消除缺失的编号
# 编写一个程序，在一个文件夹中，找到所有带指定前缀的文件， 诸如 spam001.txt,
# spam002.txt 等，并定位缺失的编号（ 例如存在 spam001.txt 和 spam003.txt，但不存
# 在 spam002.txt）。让该程序对所有后面的文件改名，消除缺失的编号。

# 作为附加的挑战，编写另一个程序，在一些连续编号的文件中，空出一些编号，
# 以便加入新的文件

re.compile(r'^spam(\d\d\d)$')
for flodername, subfloders, filenames in os.walk(floder):
    for filename in filenames:


