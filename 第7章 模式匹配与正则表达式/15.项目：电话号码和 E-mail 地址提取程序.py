# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/13 1:27 下午

# 假设你有一个无聊的任务，要在一篇长的网页或文章中，找出所有电话号码和 邮件地址。
# 。如果手动翻页，可能需要查找很长时间。如果有一个程序，可以在剪贴 板的文本中查找
# 电话号码和 E-mail 地址，那你就只要按一下 Ctrl-A 选择所有文本， 按下 Ctrl-C
# 将它复制到剪贴板，然后运行你的程序。它会用找到的电话号码和 E-mail 地址，替换掉
# 剪贴板中的文本。

# 当你开始接手一个新项目时，很容易想要直接开始写代码。但更多的时候，最好是后退一步，
# 考虑更大的图景。我建议先草拟高层次的计划，弄清楚程序需要做 什么。暂时不要思考真正
# 的代码，稍后再来考虑。现在，先关注大框架。

# 例如，你的电话号码和 E-mail 地址提取程序需要完成以下任务：
# 1.从剪贴板取得文本。
# 2.找出文本中所有的电话号码和 E-mail 地址。
# 3.将它们粘贴到剪贴板。

# 现在你可以开始思考，如何用代码来完成工作。代码需要做下面的事情：
# 1.使用 pyperclip 模块复制和粘贴字符串。
# 2.创建两个正则表达式，一个匹配电话号码，另一个匹配 E-mail 地址。
# 3.对两个正则表达式，找到所有的匹配，而不只是第一次匹配。
# 4.将匹配的字符串整理好格式，放在一个字符串中，用于粘贴。
# 5.如果文本中没有找到匹配，显示某种消息。
# 这个列表就像项目的路线图。在编写代码时，可以独立地关注其中的每一步。
# 每一步都很好管理。它的表达方式让你知道在 Python 中如何去做。

# 第 1 步：为电话号码创建一个正则表达式
# ! python3 # phoneAndEmail.py - Finds phone numbers and email
# addresses on the clipboard.

import pyperclip, re

# 电话号码从一个“可选的”区号开始，所以区号分组跟着一个问号。
# 因为区号可能只是 3 个数字（即\d{3}），或括号中的 3 个数字（即\(\d{3}\)），
# 所以应该用管道符号连接这两部分。

# 电话号码分割字符可以是空格（\s）、短横（-）或句点（.），
# 所以这些部分也应 该用管道连接。
phoneRegex = re.compile(r'''(
        (\d{3}|\(d{3}\))?               # area code
        (\s|-|\.)?                      # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)?                      # separator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2, 5}))?   # extension
)''', re.VERBOSE)

# 第 2 步：为 E-mail 地址创建一个正则表达式
# TODO: Create email regex
# E-mail 地址的用户名1部分是一个或多个字符，字符可以包括：小写和大写字母、
# 数字、句点、下划线、百分号、加号或短横。可以将所有这些放入一个字符分类：
# [a-zA-Z0-9._%+-]。

# 域名和用户名用@符号分割2，域名3允许的字符分类要少一些，只允许字母、数字、
# 句点和短横：[a-zA-Z0-9.-]。

# 最后是“dot-com”部分（技术上称为“顶级域名”），
# 它实际上可以是“dot-anything”。它有 2 到 4 个字符。

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # 1.username
    @                 # 2.@ symbol
    [a-zA-Z0-9.-]+    # 3.domain name
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# 第 3 步：在剪贴板文本中找到所有匹配
# 既然已经指定了电话号码和电子邮件地址的正则表达式，就可以让 Python 的 re 模块
# 做辛苦的工作，查找剪贴板文本中所有的匹配。pyperclip.paste()函数将取得一个字
# 符串，内容是剪贴板上的文本，findall()正则表达式方法将返回一个元组的列表。
# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
findall = phoneRegex.findall(text)
for groups in findall:
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# 第 4 步：所有匹配连接成一个字符串，复制到剪贴板
# TODO: Copy results to te clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

# 作为一个例子， 打开你的 Web 浏览器 ， 访问 No Starch Press 的联系页面
# http://www.nostarch.com/contactus.htm。按下 Ctrl-A 选择该页的所有文本，
# 按下 Ctrl-C 将它复制到剪贴板。运行这个程序，输出看起来像这样：

# input
'''
Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and Events: conferences@nostarch.com
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
Instagram
Linkedin
Pinterest
'''

# output
'''
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
conferences@nostarch.com
info@nostarch.com
'''
