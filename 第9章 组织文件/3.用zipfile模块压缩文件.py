# 9.3 用 zipfile 模块压缩文件

# 你可能熟悉 ZIP 文件（ 带有.zip 文件扩展名）， 它可以包含许多其他文件的压缩
# 内容。压缩一个文件会减少它的大小， 这在因特网上传输时很有用。因为一个 ZIP 文
# 件可以包含多个文件和子文件夹， 所以它是一种很方便的方式， 将多个文件打包成一
# 个文件。这个文件叫做“ 归档文件”， 然后可以用作电子邮件的附件，或其他用途。

# 利用 zipfile 模块中的函数， Python 程序可以创建和打开（或解压） ZIP 文件。
# 假定你有一个名为 example.zip 的 zip 文件， 它的内容如图 9-2 所示。

# 9.3.1 读取 ZIP 文件
import os
import zipfile
from pathlib import Path

os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第9章 组织文件')
with zipfile.ZipFile('lessons.zip') as f:
    for fn in f.namelist():
        extracted_path = Path(f.extract(fn))
        extracted_path.rename(fn.encode('cp437').decode('gbk'))

z_file = zipfile.ZipFile('lessons.zip')
z_file.namelist()
spamInfo = z_file.getinfo('java╖┤╔Σ.ppt')
print(spamInfo.file_size)

# 9.3.2 从 ZIP 文件中解压缩
z_file.extractall()
z_file.close()
# 你可以向extractall()传递的一个文件夹名称，它将文件解压缩到那个文件夹，而不是当前工作
# 目录。如果传递给 extractall()方法的文件夹不存在，它会被创建。例如， 如果你用
# exampleZip.extractall('C:\\ delicious')取代处的调用，代码就会从 example.zip 中解压
# 缩文件，放到新创建的 C:\delicious 文件夹中。

# ZipFile 对象的 extract()方法从 ZIP 文件中解压缩单个文件。继续交互式环境中
# 的例子：
z_file.extract('java╖┤╔Σ.ppt')
z_file.extract('java╖┤╔Σ.ppt', 'dest')
z_file.close()
# 传递给 extract()的字符串， 必须匹配 namelist()返回的字符串列表中的一个。或
# 者，你可以向 extract()传递第二个参数， 将文件解压缩到指定的文件夹， 而不是当
# 前工作目录。如果第二个参数指定的文件夹不存在， Python 就会创建它。

# 9.3.3 创建和添加到 ZIP 文件
newZip = zipfile.ZipFile('newZip.zip', 'w')
newZip.write('java─┌▓┐└α.ppt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('java═°┬τ▒α│╠.ppt', compress_type=zipfile.ZIP_DEFLATED)
newZip.namelist()
newZip.close()