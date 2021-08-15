# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/15 6:17 下午
import os
import re

print('请输入你想要查找的内容：\n')
f = input()
p = re.compile(str(f))
for path, dir_list, file_list in os.walk('/Users/yuwanmo/PycharmProjects/ATBSWP/第8章 读写文件'):
    for file_name in file_list:
        t = open(os.path.join(path, file_name))
        for line in t.readline():
            if p.search(line) is not None:
                print(line)
