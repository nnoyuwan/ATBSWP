# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/15 9:09 上午

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)  # Out[13]: shelve.DbfilenameShelf
shelfFile['cats']
shelfFile.close()

# 就像字典一样，shelf 值有 keys()和 values()方法，返回 shelf 中键和值的类似列表的值。
# 因为这些方法返回类似列表的值，而不是真正的列表，所以应该将它们传 递给 list()函数，取
# 得列表的形式。

shelfFile = shelve.open('mydata')
list(shelfFile)
list(shelfFile.values())
