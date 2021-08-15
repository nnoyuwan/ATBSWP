# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/9 5:11 下午

# 第 1 步：从剪贴板中复制和粘贴
import pyperclip

'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''

text = pyperclip.paste()
# todo Separate lines and stars.
tlist = text.split('\n')
for i in range(len(tlist)):
    tlist[i] = '* ' + tlist[i]
join = '\n'.join(tlist)
# pyperclip.copy(join)
print(join)
