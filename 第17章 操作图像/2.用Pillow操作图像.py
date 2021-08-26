import os
from PIL import Image

os.getcwd()
os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第17章 操作图像')
# 17.2.1 处理 Image 数据类型
catIm = Image.open('zophie.png')  # type:Image.Image
print(catIm.size)  # (816, 1088)
width, height = catIm.size
print(width)
print(height)
# filename 属性描述了原始文件的名称。 format 和
# format_description 属性是字符串， 描述了原始文件的图
# 像格式（ format_description 比较详细）
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)  # Portable network graphics
catIm.save('Zophie.jpg')

# Pillow 还提供了 Image.new()函数，它返回一个 Image 对象。这很像 Image.open()，
# 不过 Image.new()返回的对象表示空白的图像。 Image.new()的参数如下：
# • 字符串'RGBA'，将颜色模式设置为 RGBA（还有其他模式，但本书没有涉及）。
# • 大小，是两个整数元组，作为新图像的宽度和高度。
# • 图像开始采用的背景颜色，是一个表示 RGBA 值的四整数元组。你可以用
# ImageColor.getcolor()函数的返回值作为这个参数。另外， Image.new()也支持传
# 入标准颜色名称的字符串。

image = Image.new('RGBA', (100, 200), 'purple')
assert isinstance(image, Image.Image)
image.save('purpleImage.png')
# 如果未指定颜色参数，默认的颜色是不可见的黑色（ 0， 0， 0， 0）
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')

# 17.2.2 裁剪图片
# 矩形元组（这里就是要裁剪的区域）包括左列和顶行
# 的像素，直至但不包括右列和底行的像素()。
crop = catIm.crop((335, 345, 565, 560))
crop.save('cropped.png')

# 17.2.3 复制和粘贴图像到其他图像
catCopyIm = catIm.copy()
# catIm 和 catCopyIm 变量包含了两个独立的 Image 对象，它们的图像相同。既然
# catCopyIm 中保存了一个 Image 对象，你可以随意修改 catCopyIm，将它存入一个新的
# 文件名，而 zophie.png 没有改变。例如，让我们尝试用 paste()方法修改 catCopyIm。

faceIm = catIm.crop((335, 345, 565, 560))
print(faceIm.size)  # (230, 215)
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')

# 现在，我们可以将 faceIm 粘贴到 catCopyIm。 paste()方法有两个参数：一个“源
# Image 对象，一个包含 x 和 y 坐标的元组，指明源 Image 对象粘贴到主 Image 对象
# 时左上角的位置。

# 注意 尽管名称是 copy()和 paste()，但 Pillow 中的方法不使用计算机的剪贴板。

# 请注意， paste()方法在原图上修改它的 Image 对象，它不会返回粘贴后图像的
# Image 对象。如果想调用 paste()，但还要保持原始图像的未修改版本，就需要先复
# 制图像，然后在副本上调用 paste()。

# 假定要用 Zophie 的头平铺整个图像，如图 17-6 所示。可以用两个 for 循环来实
# 现这个效果。继续交互式环境的例子，输入以下代码：

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.crop()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save('titled.png')

# 17.2.4 调整图像大小
width, height = catIm.size  # 816 1088
# resize()方法的元组参数中只允许整数，这就是为什么需要用 int()调用对
# 两个除以 2 的值取整。
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')  # 408*544

# 但传入 resize()的新宽度和高度不必与原始图像成比例。 svelteIm
# 变量保存了一个 Image 对象，宽度与原始图像相同，
# 但高度增加了 300 像素，让 Zophie 显得更苗条。
svelteIm = catIm.resize((width, height + 300))  # 细长
svelteIm.save('svelte.png')

# 粘贴透明像素
# 通常透明像素像白色像素一样粘贴。如果要粘贴图像有透明像素，就将该图
# 像作为第三个参数传入，这样就不会粘贴一个不透明的矩形。这个第三参数是“遮
# 罩” Image 对象。遮罩是一个 Image 对象，其中 alpha 值是有效的，但红、绿、
# 蓝值将被忽略。遮罩告诉 paste()函数哪些像素应该复制，哪些应该保持透明。遮
# 罩的高级用法超出了本书的范围，但如果你想粘贴有透明像素的图像，就再传入
# 该 Image 对象作为第三个参数。

# 17.2.5 旋转和翻转图像
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')

# 注意，当图像旋转 90 度或 270 度时，宽度和高度会变化。如果旋转其他角度，
# 图像的原始尺寸会保持。在 Windows 上，使用黑色的背景来填补旋转造成的缝隙，
# 如图 17-8 所示。在 OS X 上，使用透明的像素来填补缝隙。 rotate()方法有一个可选
# 的 expand 关键字参数，如果设置为 True，就会放大图像的尺寸，以适应整个旋转
# 后的新图像。例如，在交互式环境中输入以下代码：

catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

# 利用 transpose()方法，还可以得到图像的“镜像翻转”。必须向 transpose()方法
# 传入 Image.FLIP_LEFT_RIGHT 或 Image.FLIP_TOP_BOTTOM。
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

# 17.2.6 更改单个像素

# 单个像素的颜色可以通过 getpixel()和 putpixel()方法取得和设置。它们都接受一个元
# 组，表示像素的 x 和 y 坐标。 putpixel()方法还接受一个元组，作为该像素的颜色。
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))  # (0, 0, 0, 0)
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))
from PIL import ImageColor

for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

    im.getpixel((0, 0))
    im.getpixel((0, 50))
im.save('putPixel.png')
