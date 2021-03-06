# 即使你是一个有经验的计算机用户， 可能也会用鼠标和键盘手工处理文件。现
# 在的文件浏览器使得处理少量文件的工作很容易。但有时候，如果用计算机的浏览
# 器， 你需要完成的任务可能要花几个小时。
#
# os 和 shutil 模块提供了一些函数， 用于复制、 移动、 改名和删除文件。在删除
# 文件时， 你可能希望使用 send2trash 模块， 将文件移动到回收站或垃圾箱， 而不是
# 永久地删除它们。在编程处理文件时，最好是先注释掉实际会复制/移动/改名/删除
# 文件的代码， 添加 print()调用， 这样你就可以运行该程序， 验证它实际会做什么。
#
# 通常， 你不仅需要对一个文件夹中的文件执行这些操作， 而是对所有下级子文
# 件夹执行操作。 os.walk()函数将处理这个艰苦工作，遍历文件夹，这样你就可以专
# 注于程序需要对其中的文件做什么。
#
# zipfile 模块提供了一种方法，用 Python 压缩和解压 ZIP 归档文件。和 os 和 shutil
# 模块中的文件处理函数一起使用， 很容易将硬盘上任意位置的一些文件打包。和许
# 多独立的文件相比， 这些 ZIP 文件更容易上传到网站， 或作为 E-mail 附件发送。
# 本书前面几章提供了源代码让你拷贝。但如果你编写自己的程序， 可能在第一
# 次编写时不会完美无缺。 下一章将聚焦于一些 Python 模块，它们帮助你分析和调试
# 程序， 这样就能让程序很快正确运行。

