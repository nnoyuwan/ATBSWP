# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/15 5:04 下午

# 8.9.1 扩展多重剪贴板
#
# 扩展本章中的多重剪贴板程序，增加一个 delete <keyword>命令行参数，它将从
# shelf 中删除一个关键字。然后添加一个 delete 命令行参数，它将删除所有关键字。

# ! python3 # mcb.pyw - Saves and loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.

#        py.exe mcb.pyw delete <keyword> - Loads keyword to clipboard.

#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.

import pyperclip
import shelve
import sys

mcbShelf = shelve.open('mcb')

# todo save clipbpard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        s = str(list(mcbShelf.keys()))
        pyperclip.copy(s)
    # 扩展本章中的多重剪贴板程序，增加一个 delete <keyword>命令行参数，它将从
    # # shelf 中删除一个关键字。然后添加一个 delete 命令行参数，它将删除所有关键字。
    elif sys.argv[1].lower() == 'delete':
        for k in mcbShelf.keys():
            del mcbShelf[k]

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # todo: list keywords and load content

mcbShelf.close()

