# 如果需要在图像上画线、矩形、圆形或其他简单形状，就用 Pillow 的 ImageDraw 模
# 块。在交互式环境中输入以下代码：

from PIL import Image, ImageDraw

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# 我们将该 Image 对
# 象传入 ImageDraw.Draw()函数，得到一个 ImageDraw 对象。这个对象有一些方法，
# 可以在 Image 对象上绘制形状和文字。将 ImageDraw 对象保存在变量 draw 中，这
# 样就能在接下来的例子中方便地使用

# 17.4.1 绘制形状

# 下面的 ImageDraw 方法在图像上绘制各种形状。这些方法的 fill 和 outline 参数
# 是可选的，如果未指定，默认为白色。

# 点
# point(xy, fill)方法绘制单个像素。 xy 参数表示要画的点的列表。该列表可以是 x
# 和 y 坐标的元组的列表，例如[(x, y), (x, y), ...]，或是没有元组的 x 和 y 坐标的列表，
# 例如[x1, y1, x2, y2, ...]。 fill 参数是点的颜色，要么是一个 RGBA 元组，要么是颜色
# 名称的字符串，如'red'。 fill 参数是可选的。

# 线
# line(xy, fill, width)方法绘制一条线或一系列的线。 xy 要么是一个元组的列表，
# 例如[(x, y), (x, y), ...]，要么是一个整数列表，例如[x1, y1, x2, y2, ...]。每个点都是正
# 在绘制的线上的一个连接点。可选的 fill 参数是线的颜色，是一个 RGBA 元组或颜色
# 名称。可选的 width 参数是线的宽度，如果未指定，缺省值为 1。

# 矩形
# rectangle(xy, fill, outline)方法绘制一个矩形。 xy 参数是一个矩形元组，形式为(left,
# top, right, bottom)。 left 和 top 值指定了矩形左上角的 x 和 y 坐标， right 和 bottom 指定
# 了矩形的右下角。

# 椭圆
# ellipse(xy, fill, outline)方法绘制一个椭圆。如果椭圆的宽度和高度一样，该方法将绘
# 制一个圆。 xy 参数是一个矩形元组(left, top, right, bottom)，它表示正好包含该椭圆的
# 矩形。

# 多边形
# polygon(xy, fill, outline)方法绘制任意的多边形。 xy 参数是一个元组列表，例如
# [(x, y), (x, y), ...]，或者是一个整数列表，例如[x1, y1, x2, y2, ...]，表示多边形边的连
# 接点。最后一对坐标将自动连接到第一对坐标。可选的 fill 参数是多边形内部的颜
# 色，可选的 outline 参数是多边形轮廓的颜色。

# 绘制示例
# 在交互式环境中输入以下代码：

# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
# draw.rectangle((20, 30, 60, 60), fill='blue')
# draw.ellipse((120, 30, 160, 60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i - 100)], fill='green')
# im.save('drawing.png')


# 17.4.2 绘制文本
from PIL import Image, ImageDraw, ImageFont
import os

# ImageDraw 对象还有 text()方法，用于在图像上绘制文本。 text()方法有 4 个参
# 数： xy、 text、 fill 和 font。
# • xy 参数是两个整数的元组，指定文本区域的左上角。
# • text 参数是想写入的文本字符串。
# • 可选参数 fill 是文本的颜色。
# • 可选参数 font 是一个 ImageFont 对象，用于设置文本的字体和大小。

draw.text((20, 150), 'Hello', fill='purple')
fontsFloder = 'C:\\Windows\\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFloder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('text.png')

# 因为通常很难预先知道一块文本在给定的字体下的大小，所以 ImageDraw 模块
# 也提供了 textsize()方法。它的第一个参数是要测量的文本字符串，第二个参数是可
# 选的 ImageFont 对象。 textsize()方法返回一个两整数元组，表示如果以指定的字体
# 写入图像，文本的宽度和高度。可以利用这个宽度和高度，帮助你精确计算文本放
# 在图像上的位置。

# 既然已经导入 Pillow 的 ImageFont 模块，就可以调用 ImageFont.truetype()函数，它
# 有两个参数。
# 第一个参数是字符串，表示字体的 TrueType 文件，这是硬盘上实际的字
# 体文件。 TrueType 字体文件具有.TTF 文件扩展名，通常可以在以下文件夹中找到：

# • 在 Windows 上： C:\Windows\Fonts。
# • 在 OS X 上： /Library/Fonts and /System/Library/Fonts。
# • 在 Linux 上： /usr/share/fonts/truetype。

# 实际上并不需要输入这些路径作为 TrueType 字体文件的字符串的一部分，因为
# Python 知道自动在这些目录中搜索字体。如果无法找到指定的字体， Python 会显示错误。
#
# ImageFont.truetype()的第二个参数是一个整数，表示字体大小的点数（而不是像
# 素）。请记住， Pillow 创建的 PNG 图像默认是每英寸 72 像素，一点是 1/72 英寸。
