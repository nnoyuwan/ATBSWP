# 假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期
# （ MM-DD-YYYY），需要将它们改名为欧洲风格的日期（ DD-MM-YYYY）。手工 完
# 成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。

# ! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1)?\d)-                        # one or two digits for the month
((0|1|2|3)?\d)-                      # one or two digits for the day
((19|20)\d\d)                       # four digits for the year
(.*?)$
""", re.VERBOSE)
# datePattern.search('spam4-4-1984.txt')
# datePattern.search('01-03-2014eggs.zip')

# shutil.move()函数可以用于文件改名： 它的参数是要改名的文件
# 名，以及新的文件名。

# 正则表达式字符串以^(.*?)开始，匹配文件名开始处、日期出现之前的任何文本。
# ((0|1)?\d)分组匹配月份。第一个数字可以是 0 或 1， 所以正则表达式匹配 12，作为
# 十二月份， 也会匹配 02， 作为二月份。这个数字也是可选的， 所以四月份可以是
# 04 或 4。日期的分组是((0|1|2|3)?\d)，它遵循类似的逻辑。 3、 03 和 31 是有效的日期
# 数字（是的， 这个正则表达式会接受一些无效的日期，诸如 4-31-2014、 2-29-2013
# 和 0-15-2014。 日期有许多特例，很容易被遗漏。为了简单，这个程序中的正则表
# 达式已经足够好了）。

# 虽然 1885 是一个有效的年份， 但你可能只在寻找 20 世纪和 21 世纪的年份。
# 这防止了程序不小心匹配非日期的文件名，它们和日期格式类似， 诸如
# 10-10-1000.txt。

# 正则表达式的(.*?)$部分， 将匹配日期之后的任何文本。

# TODO: Loop over the files in the working directory.

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo is None:
        # TODO: Skip files without a date.
        continue
    # TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # 为了让分组编号直观， 请尝试从头阅读该正则表达式， 每遇到一个左括号就计数加
    # 一。不要考虑代码， 只是写下该正则表达式的框架。
    # datePattern = re.compile(r"""^(1) # all text before the date
    # (2 (3) )- # one or two digits for the month
    # (4 (5) )- # one or two digits for the day
    # (6 (7) ) # four digits for the year
    # (8)$ # all text after the date
    # """, re.VERBOSE)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename)  # uncomment after testing
