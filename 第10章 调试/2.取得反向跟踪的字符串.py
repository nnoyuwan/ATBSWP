# 如果 Python 遇到错误，它就会生成一些错误信息，称为“反向跟踪”。反向跟踪
# 包含了出错消息、导致该错误的代码行号，以及导致该错误的函数调用的序列。这
# 个序列称为“调用栈”。


def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


spam()

# 在从多个位置调用函数的程序中，调用栈就能帮助你确定哪次调用导致了错误。


# 只要抛出的异常没有被处理， Python 就会显示反向跟踪。但你也可以调用
# traceback.format_exc()，得到它的字符串形式。如果你希望得到异常的反向跟踪的信
# 息，但也希望 except 语句优雅地处理该异常，这个函数就很有用。在调用该函数之
# 前，需要导入 Python 的 traceback 模块。

# 例如，不是让程序在异常发生时就崩溃，可以将反向跟踪信息写入一个日志文
# 件，并让程序继续运行。稍后，在准备调试程序时，可以检查该日志文件。在交互
# 式环境中输入以下代码：

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')
