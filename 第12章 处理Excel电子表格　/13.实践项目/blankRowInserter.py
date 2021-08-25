# 创建一个程序 blankRowInserter.py，它接受两个整数和一个文件名字符串作为
# 命令行参数。我们将第一个整数称为 N，第二个整数称为 M。程序应该从第 N 行开
# 始，在电子表格中插入 M 个空行。例如，如果这样执行程序：
import sys

import openpyxl

param = sys.argv[1:3]
param = list(map(int, param))

wb = openpyxl.load_workbook('myProduce.xlsx')
sheet = wb.active
# n_rows = sheet.max_row

sheet.insert_rows(param[0], param[1])
wb.save('myProduce_.xlsx')
