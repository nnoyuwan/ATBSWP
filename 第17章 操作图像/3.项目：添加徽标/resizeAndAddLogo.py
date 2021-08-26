# 假设你有一项无聊的工作，要调整数千张图片的大小，并在每张图片的角上增
# 加一个小徽标水印。使用基本的图形程序，如 Paintbrush 或 Paint，完成这项工作需
# 要很长时间。像 Photoshop 这样神奇的应用程序可以批量处理，但这个软件要花几
# 百美元。让我们写一个脚本来完成工作。

# 总的来说，程序应该完成下面的事：
# • 载入徽标图像。
# • 循环遍历工作目标中的所有.png 和.jpg 文件。
# • 检查图片是否宽于或高于 300 像素。
# • 如果是，将宽度或高度中较大的一个减小为 300 像素，并按比例缩小的另一维度。
# • 在角上粘贴徽标图像。
# • 将改变的图像存入另一个文件夹。

# 这意味着代码需要做到以下几点：
# • 打开 catlogo.png 文件作为 Image 对象。
# • 循环遍历 os.listdir('.')返回的字符串。
# • 通过 size 属性取得图像的宽度和高度。
# • 计算调整后图像的新高度和宽度。
# • 调用 resize()方法来调整图像大小。
# • 调用 paste()方法来粘贴徽标。
# • 调用 save()方法保存更改，使用原来的文件名。


# 第 1 步：打开徽标图像
# ! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image
import os

os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第17章 操作图像')
# os.getcwd()
# # 在程序开始时设置 SQUARE_FIT_SIZE和 LOGO_FILENAME常量，这让程
# # 序以后更容易修改。假定你要添加的徽标不是猫图标，或者假定将输出图像的最大
# # 大小要减少的值不是 300 像素。有了程序开始时定义的这些常量，你可以打开代码，
# # 修改一下这些值，就大功告成了（或者你可以让这些常量的值从命令行参数获得）。
# # 没有这些常数，就要在代码中寻找所有的 300 和'catlogo.png'，将它们替换新项目的
# # 值。总之，使用常量使程序更加通用。
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第17章 操作图像\\3.项目：添加徽标\\catlogo.png'
logoIm = Image.open(LOGO_FILENAME)
assert isinstance(logoIm, Image.Image)
logoIm = logoIm.resize((50, 50))

assert isinstance(logoIm, Image.Image)
logoWidth, logoHeight = logoIm.size
print(logoIm.size)

# 1.Loop over all files in the working directory.
os.makedirs('withLogo', exist_ok=True)
for fn in os.listdir('C:\\Users\\admin\PycharmProjects\\ATBSWP\\第17章 操作图像'):
    print(fn)
    if not (fn.endswith('png') or fn.endswith('jpg')):
        continue
    im = Image.open(fn)
    assert isinstance(im, Image.Image)
    width, height = im.size
    # 2.Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # 如果图像确实需要调整大小，就需要弄清楚它是太宽还是太高。如果 width 大
        # 于 height，则高度应该根据宽度同比例减小

        # 3.Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing %s...' % fn)
        # 4.Resize the image.
        im = im.resize((width, height))

        # 5.Add the logo.
        # 不论图像是否调整大小，徽标仍应粘贴到右下角。徽标粘贴的确切位置取决于
        # 图像的大小和徽标的大小。图 17-12 展示了如何计算粘贴的位置。粘贴徽标的左坐
        # 标将是图像宽度减去徽标宽度，顶坐标将是图像高度减去徽标高度。
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        # 6.Save changes
        im.save(os.path.join('withLogo', fn))
