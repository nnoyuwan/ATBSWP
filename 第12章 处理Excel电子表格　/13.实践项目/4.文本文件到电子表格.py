import os, openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

wb = openpyxl.Workbook()
sheet = wb.active

os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第12章 处理Excel电子表格　\\13.实践项目')
n = 1
with open('errorInfo.txt', 'r') as f1:
    for line in f1.readlines():
        sheet['A' + str(n)].value = line
        n += 1

n = 1
with open('python_path.txt', 'r') as f2:
    for line in f2.readlines():
        sheet['B' + str(n)].value = line
        n += 1

wb.save('txt2excel.xlsx')
