# 1．写一条 assert 语句，如果变量 spam 是一个小于 10 的整数，就触发AssertionError。
import re

spam = 20
assert spam < 10, 'spam need lower than 10'

# 2．编写一条 assert 语句，如果 eggs 和 bacon 包含的字符串彼此相同，而且不
# 论大小写如何，就触发 AssertionError（也就是说， 'hello' 和 'hello' 被认为相同，
# 'goodbye' 和 'GOODbye' 也被认为相同）。

eggs = 'abcD'
bacon = 'Abc'
assert re.compile(eggs).search(bacon), 'eggs != bacon'

# 3．编写一条 assert 语句，总是触发 AssertionError。
# assert False, 'always show error!'


# 4．为了能调用 logging.debug()，程序中必须加入哪两行代码？

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 5．为了 让 logging.debug() 将日志消息发送到名为 programLog.txt 的文件中，程
# 序必须加入哪两行代码？
import logging

logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
