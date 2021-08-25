# 设置某些单元格行或列的字体风格，可以帮助你强调电子表格中重点的区域。
# 例如，在这个产品电子表格中，程序可以对 potato、 garlic 和 parsnip 等行使用粗体。
# 或者也许你希望对每磅价格超过 5 美元的行使用斜体。手工为大型电子表格的某些
# 部分设置字体风格非常令人厌烦，但程序可以马上完成。
# 为了定义单元格的字体风格，需要从 openpyxl.styles 模块导入 Font()和 Style()
# 函数。

import openpyxl, os
from openpyxl.styles import Font

os.getcwd()
os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第12章 处理Excel电子表格　')
wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font
sheet['A1'] = 'Hello world!'
sheet.column_dimensions['A'].font = italic24Font
wb.save('styled.xlsx')

# 补充： 如果要对A列进行格式设置，则代码书写为：sheet.column_dimensions['A'].font = italic24Font。
