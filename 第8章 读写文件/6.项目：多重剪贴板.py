# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/15 1:04 下午

# 假定你有一个无聊的任务，要填充一个网页或软件中的许多表格，其中包含一些文本字段。
# 剪贴板让你不必一次又一次输入同样的文本，但剪贴板上一次只有一 个内容。如果你有几
# 段不同的文本需要拷贝粘贴，就不得不一次又一次的标记和拷 贝几个同样的内容。

# 该程序将利用一个关键字保存每段剪贴板文本。例如，当运行 py mcb.pyw save spam，
# 剪贴板中当前的内容就用关键字 spam 保存。通过运行 py mcb.pyw spam，这段文本
# 稍后将重新加载到剪贴板中。如果用户忘记了都有哪些关键字，他们可以运行 py mcb.pyw list，
# 将所有关键字的列表复制到剪贴板中。

# 第 1 步：注释和 shelf 设置
# ! python3 # mcb.pyw - Saves and loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.

#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# todo save clipbpard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # todo: list keywords and load content

mcbShelf.close()

# 将一般用法信息放在文件顶部的注释中，这是常见的做法。如果忘了如何运 行这个脚本，就可以看看这些注释，帮助回忆起来。

