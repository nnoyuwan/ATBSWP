# 编写一个程序，遍历硬盘上的每个文件夹，找到可能的照片文件夹。当然，首
# 先你必须定义什么是“照片文件夹”。假定就是超过半数文件是照片的任何文件夹。
# 你如何定义什么文件是照片？

# 首先，照片文件必须具有文件扩展名.png 或.jpg。此外，照片是很大的图像。
# 照片文件的宽度和高度都必须大于 500 像素。这是安全的假定，因为大多数数码相
# 机照片，宽度和高度都是几千像素。

# 作为提示，下面是这个程序的粗略框架：
from PIL import Image
import os

dir = 'C:\\Users\\admin\\PycharmProjects\\ATBSWP'
for flodername, subfloders, filenames in os.walk(dir):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    # Check if file extension isn't .png or .jpg.
    for fn in filenames:
        if not (
                fn.endswith('png') or
                fn.endswith('jpg') or
                fn.endswith('JPG') or
                fn.endswith('PNG')
        ):
            numNonPhotoFiles += 1
            continue
        # Open image file using Pillow.
        im = Image.open(os.path.join(flodername, fn))
        assert isinstance(im, Image.Image)
        # Check if width & height are larger than 500.
        if im.size[0] > 500 and im.size[1] > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1

    if numPhotoFiles > numNonPhotoFiles:
        print(flodername)


