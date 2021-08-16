# 9.1.1 复制文件和文件夹

# shutil 模块提供了一些函数，用于复制文件和整个文件夹。调用shutil.copy(source, destination)，
# 将路径 source 处的文件复制到路径 destination处的文件夹
# （ source 和 destination 都是字符串）。如果 destination
# 是一个文件名，它将作为被复制文件的新名字。该函数返回一个字符串，表示被复制文件的路径。

import os
import shutil

os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第9章 组织文件')
copy = shutil.copy('spam.txt', 'dest')
print(copy)
copy = shutil.copy('spam.txt', 'dest\\spam1.txt')
print(copy)

# shutil.copy()将复制一个文件， shutil.copytree()将复制整个文件夹，以及它包含
# 的文件夹和文件。调用 shutil.copytree(source, destination)，将路径 source 处的文件
# 夹，包括它的所有文件和子文件夹，复制到路径 destination 处的文件夹。 source 和
# destination 参数都是字符串。该函数返回一个字符串，是新复制的文件夹的路径。

shutil.copytree('dest', 'dest2')

# 9.1.2 文件和文件夹的移动与改名

# 如果 destination 指向一个文件夹， source文件将移动到
# destination 中， 并保持原来的文件名。
shutil.move('eggs.txt', 'dest2')

# destination 路径也可以指定一个文件名。在下面的例子中，
# source 文件被移动并改名
shutil.move('dest2\\eggs.txt', 'dest\\eggs_rename.txt')  # 'dest2\\eggs.txt'

# 前面两个例子都假设在 C:\目录下有一个文件夹 dest。但是如果没有 dest 文件
# 夹， move()就会将 bacon.txt 改名，变成名为 dest5 的文件。
shutil.move('dest\\eggs_rename.txt', 'dest5')  # 'dest2\\eggs.txt'

# 这里， move()在 C:\目录下找不到名为 dest5 的文件夹， 所以假定 destination 指
# 的是一个文件， 而非文件夹。所以 eggs_rename.txt 文本文件被改名为 dest5（没有.txt 文件
# 扩展名的文本文件）， 但这可能不是你所希望的！ 这可能是程序中很难发现的缺陷，
# 因为 move()调用会很开心地做一些事情， 但和你所期望的完全不同。这也是在使用
# move()时要小心的另一个理由。


# 9.1.3 永久删除文件和文件夹
# 利用 os 模块中的函数，可以删除一个文件或一个空文件夹。但利用 shutil 模块，
# 可以删除一个文件夹及其所有的内容。

# • 用 os.unlink(path)将删除 path 处的文件。
# • 调用 os.rmdir(path)将删除 path 处的文件夹。该文件夹必须为空，其中没有任
# 何文件和文件夹。
# • 调用 shutil.rmtree(path)将删除 path 处的文件夹，它包含的所有文件和文件夹都
# 会被删除。


# 在程序中使用这些函数时要小心！可以第一次运行程序时， 注释掉这些调用，
# 并且加上 print()调用， 显示会被删除的文件。 这样做是一个好主意。下面有一个
# Python 程序，本来打算删除具有.txt 扩展名的文件， 但有一处录入错误（ 用粗体突
# 出显示 ）， 结果导致它删除了.rxt 文件。
import os

for filename in os.listdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第9章 组织文件\\dest'):
    if filename.endswith('rxt'):
        os.unlink(filename)

# 如果你有某些重要的文件以.rxt 结尾，它们就会被不小心永久地删除。作为替
# 代，你应该先运行像这样的程序：

# 在确定程序按照你的意图工作后 ， 删除 print(filename) 代码行 ， 取消
# os.unlink(filename)代码行的注释。 然后再次运行该程序，实际删除这些文件。
for filename in os.listdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第9章 组织文件\\dest'):
    if filename.endswith('.rxt'):
        # os.unlink(filename)
        print(filename)

# 9.1.4 用 send2trash 模块安全地删除
# 因为 Python 内建的 shutil.rmtree()函数不可恢复地删除文件和文件夹，所以 用起
# 来可能有危险。删除文件和文件夹的更好方法，是使用第三方的 send2trash 模块。
# 你可以在终端窗口中运行 pip install send2trash，安装该模块

# 利用 send2trash，比 Python 常规的删除函数要安全得多，因为它会将文件夹和文件发送到计算机的垃圾箱或回收站，而不是永久删除它们。如果因程序缺陷而用
# send2trash 删除了某些你不想删除的东西，稍后可以从垃圾箱恢复。

import send2trash

os.getcwd()
baconFile = open('dest5', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('dest5')
