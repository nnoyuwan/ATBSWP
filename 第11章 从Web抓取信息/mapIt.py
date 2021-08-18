# 第 1 步：弄清楚 URL

# 根据附录 B 中的指导，建立 mapIt.py，这样当你从命令行运行它时，例如
# C:\> mapit 870 Valencia St, San Francisco, CA 94110

# 该脚本将使用命令行参数，而不是剪贴板。如果没有命令行参数，程序就知道
# 要使用剪贴板的内容。
# 首先你需要弄清楚，对于指定的街道地址，要使用怎样的 URL。你在浏览器中打
# 开 http://maps.google.com/并查找一个地址时，地址栏中的 URL 看起来就像这样： https://
# www.google.com/maps/place/870+Valencia+St/@37.7590311,-122.4215096, 17z/data=
# !3m1!4b1!4m2!3m1!1s0x808f7e3dadc07a37:0xc86b0b2bb93b73d8.
# 地址就在 URL 中，但其中还有许多附加的文本。网站常常在 URL 中添加额外
# 的数据，帮助追踪访问者或定制网站。但如果你尝试使用 https://www.google.
# com/maps/place/870+Valencia+St+San+Francisco+CA/，会发现仍然可以到达正确的页
# 面。所以你的程序可以设置为打开一个浏览器，访问 'https://www.google.com/
# maps/place/your_address_string'（其中 your_address_string 是想查看地图的地址）。


# 第 2 步：处理命令行参数
import webbrowser, sys

import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    # Get address from command line.
    address = pyperclip.paste()

# 命令行参数通常用空格分隔，但在这个例子中，你希望将所有参数解释为一个字符串。
# 因为 sys.argv 是字符串的列表，所以你可以将它传递给 join()方法，这将返回一个字符串。
# 你不希望程序的名称出现在这个字符串中，所以不是使用 sys.argv，而是使用 sys.argv[1:]，
# 砍掉这个数组的第一个元素。这个表达式求值得到的字符串，保存在 address 变量中。

# 如果运行程序时在命令行中输入以下内容：
# mapit 870 Valencia St, San Francisco, CA 94110
# …sys.argv 变量将包含这样的列表值：
# ['mapIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco, ', 'CA', '94110']

webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(
    'google.com/maps/place/' + address)
# webbrowser.open('google.com')

# cml:python mapit.py 870 Valencia St, San Francisco, CA 94110
# cml:python mapit.py 台湾台北市大安区安居街84巷


# 表 11-1 不用和利用 mapIt.py 取得地图
# 手工取得地图                    利用 mapIt.py
# 高亮标记地址                    高亮标记地址
# 拷贝地址                       拷贝地址
# 打开 Web 浏览器                 运行 mapIt.py
# 打开 http://maps.google.com/
# 点击地址文本字段
# 拷贝地址
# 按回车


# 第 4 步：类似程序的想法
# 只要你有一个 URL， webbrowser 模块就让用户不必打开浏览器，而直接加载一
# 个网站。其他程序可以利用这项功能完成以下任务：
# • 在独立的浏览器标签中，打开一个页面中的所有链接。
# • 用浏览器打开本地天气的 URL。
# • 打开你经常查看的几个社交网站。
