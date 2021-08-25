# Font 对象的 style 属性影响文本在单元格中的显示方式。要设置字体风格属性，就
# 向 Font()函数传入关键字参数。表 12-2 展示了 Font()函数可能的关键字参数。


# 表 12-2 Font style 属性的关键字参数
# 关键字参数         数据类型        描述
# name              字符串         字体名称，诸如'Calibri'或'Times New Roman'
# size              整型           大小点数
# bold              布尔型         True 表示粗体
# italic            布尔型         True 表示斜体


# 可以调用 Font()来创建一个 Font 对象，并将这个 Font 对象保存在一个变量中。
# 然后将它传递给 Style()，得到 的 Style 对象保存在一个变量中，并将该变量赋给 Cell
# 对象的 style 属性。例如，下面的代码创建了各种字体风格：
import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']

fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = fontObj1
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['B3'].font = fontObj2
sheet['B3'] = '24 pt Italic'

wb.save('Style.xlsx')
