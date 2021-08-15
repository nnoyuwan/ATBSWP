# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/15 6:10 下午

import re

# 8.9.2 疯狂填词
# 创建一个疯狂填词（Mad Libs）程序，它将读入文本文件，并让用户在该文本文件中出现 ADJECTIVE、NOUN、ADVERB 或 VERB
# 等单词的地方，加上他们自 己的文本。例如，一个文本文件可能看起来像这样：

# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.
#
# 程序将找到这些出现的单词，并提示用户取代它们。
#
# Enter an adjective: silly
# Enter a noun: chandelier
# Enter a verb: screamed
# Enter a noun: pickup truck

# 以下的文本文件将被创建：
#
# The silly panda walked to the chandelier and then screamed.
# A nearby pickup truck was unaffected by these events.
#
# 结果应该打印到屏幕上，并保存为一个新的文本文件。

p = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
t = open('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件/Mad Libs.txt')
s = t.read()
print(s)
l = p.findall(s)
for i in l:
    print('Enter an ' + i.lower() + " :")
    i_ = l[l.index(i)]
    p1 = re.compile(i_)
    s = p1.sub(input(), s)
print(s)
