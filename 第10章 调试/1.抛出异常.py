# 程序员之间流传着一个老笑话：“编码占了编程工作量的
# 90%，调试占了另外 90%。”

# 其次，你要学习如何使用调试器。调试器是 IDLE 的一项功能，它可以一次执
# 行一条指令，在代码运行时，让你有机会检查变量的值，并追踪程序运行时值的变
# 化。这比程序全速运行要慢得多，但可以帮助你查看程序运行时其中实际的值，而
# 不是通过源代码推测值可能是什么

# raise Exception('This is the message.')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
