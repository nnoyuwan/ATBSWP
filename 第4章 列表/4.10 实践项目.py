# 4.10.1 逗号代码
# spam = ['apples', 'bananas', 'tofu', 'cats']
#
#
# def concatElem(list):
#     s = ''
#     for e in list:
#         if list.index(e) == len(list) - 2:
#             s = s + e + ', and '
#         elif list.index(e) != len(list) - 1:
#             s = s + e + ', '
#         else:
#             s = s + e
#     return s
#
#
# res = concatElem(spam)
# res

# 4.10.2 字符图网格
import numpy as np

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# res = np.asarray(grid).T
# print(res)


def transpose(array2d):
    res = []
    for i in range(len(array2d[1])):
        array1d = []
        for j in range(len(array2d) - 1, -1, -1):
            array1d.append(array2d[j][i])
        res.append(array1d)
    return res


res = transpose(grid)
print(np.asarray(res))
