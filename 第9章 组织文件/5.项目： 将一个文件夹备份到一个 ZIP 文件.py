# 假定你正在做一个项目，它的文件保存在 C:\AlsPythonBook 文件夹中。你担心工作
# 会丢失， 所以希望为整个文件夹创建一个 ZIP 文件， 作为“快照” 。你希望保存不同的版
# 本， 希望 ZIP 文件的文件名每次创建时都有所变化。例如 AlsPythonBook_1.zip、
# AlsPythonBook_2.zip、 AlsPythonBook_3.zip， 等等。你可以手工完成， 但这有点烦人，
# 而且可能不小心弄错 ZIP 文件的编号。运行一个程序来完成这个烦人的任务会简单得多。

# 第 1 步：弄清楚 ZIP 文件的名称
import zipfile, os


def backToZip(floder):
    # Backup the entire contents of "floder" into ZIP file
    floder = os.path.abspath(floder)  # make sure floder is absolute

    # Figure out the filename this code should use based on
    # what files already exist
    number = 1
    zipFilename = ''
    while True:
        # 通过检查 delicious_1.zip 是否存在， 然后检查 delicious_2.zip 是否存在， 继续下
        # 去， 可以确定 N 应该是什么。
        zipFilename = os.path.basename(floder) + ' ' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    # 第 2 步：创建新 ZIP 文件
    # Create the ZIP file.
    print('Creating %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(floder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(floder) + '_'
            if filename.startwith(newBase) and filename.endwith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print('Done.')

# backupToZip('C:\\delicious')
