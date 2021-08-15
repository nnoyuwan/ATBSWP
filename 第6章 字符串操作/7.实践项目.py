# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/11 5:10 下午

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

rjust_size = []


def printTable(str_lists):
    print(len(str_lists))
    print(len(str_lists[0]))
    for str_list in str_lists:
        ele_size = []
        for s in str_list:
            ele_size.append(len(s))
        rjust_size.append(max(ele_size))

    for i in range(len(str_list[0])):
        for j in range(len(str_lists)):
            if j == 0:
                print(str_lists[j][i].rjust(rjust_size[j]), end=' ')
            else:
                print(str_lists[j][i].ljust(rjust_size[j]), end=' ')

        print()


printTable(tableData)
# def rjustFormat(g):
#     rjsize = []
#     for i in range(len(g)):
#         elesize = []
#         for j in range(len(g[i])):
#             elesize = elesize + [len(g[i][j])]
#             rjsize = rjsize + [max(elesize)]
#
#     for j in range(len(g[i])):
#         for i in range(len(g)):
#             print(g[i][j].rjust(max(rjsize)), end=' ')
#         print(end='\n')
#
#
# rjustFormat(tableData)
