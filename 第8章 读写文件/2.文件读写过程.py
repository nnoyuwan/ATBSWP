# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/15 8:23 上午

# “纯文本文件”只包含基本文本字符，不包含字 体、大小和颜色信息。带有.txt 扩展名的文本文件，
# 以及带有.py 扩展名的 Python 脚本 文件，都是纯文本文件的例子。它们可以被 Windows 的
# Notepad 或 OS X 的 TextEdit 应用打开。你的程序可以轻易地读取纯文本文件的内容，将它们
# 作为普通的字符串值。

# “二进制文件”是所有其他文件类型，诸如字处理文档、PDF、图像、电子表格和可执行程序。
# 如果用 Notepad 或 TextEdit 打开一个二进制文件，它看起来就像乱码，如图 8-5 所示。
# ![](https://moyuwan-image.oss-cn-hangzhou.aliyuncs.com/img/20210815082943.png)

# 既然每种不同类型的二进制文件，都必须用它自己的方式来处理，本书就不会探讨直接读写二进制文件。
# 好在，许多模块让二进制文件的处理变得更容易。在本章稍后，你将探索其中一个模块：shelve。

# 在 Python 中，读写文件有 3 个步骤： 1．调用 open()函数，返回一个 File 对象。 2．调用 File 对象的
# read()或 write()方法。 3．调用 File 对象的 close()方法，关闭该文件。

# 8.2.1 用 open()函数打开文件
file = open('/Users/yuwanmo/Library/Containers/com.apple.TextEdit/Data/Documents/_sidebar 3')

# 8.2.2 读取文件内容
content = file.read()
print(content)

file.seek(0)
lines = file.readlines()
for line in lines:
    print(line)
file.close()

# 8.2.3 写入文件
wfile = open('/Users/yuwanmo/Library/Containers/com.apple.TextEdit/Data/Documents/_sidebar 4.txt')
wfile.write('Hello world!\n')  # io.UnsupportedOperation: not writable
wfile.close()

# 你需要以“写入纯文本模 式”或“添加纯文本模式”打开该文件，或简称为“写模式”和“添加模式”。
wfile = open('/Users/yuwanmo/Library/Containers/com.apple.TextEdit/Data/Documents/_sidebar 4.txt', 'w')  # 覆盖
wfile.write('Hello world!\n')
wfile.close()

wfile = open('/Users/yuwanmo/Library/Containers/com.apple.TextEdit/Data/Documents/_sidebar 4.txt', 'a')  # 追加
wfile.write('append content\n')
wfile.close()
