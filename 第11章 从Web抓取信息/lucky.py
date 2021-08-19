# 每次我在 Google 上搜索一个主题时，都不会一次只看一个搜索结果。通过鼠
# 标中键点击搜索结果链接，或在点击时按住 CTRL 键，我会在一些新的选项卡中打
# 开前几个链接，稍后再来查看。我经常搜索 Google，所以这个工作流程（开浏览器，
# 查找一个主题，依次用中键点击几个链接）变得很乏味。如果我只要在命令行中输
# 入查找主题，就能让计算机自动打开浏览器，并在新的选项卡中显示前面几项查询
# 结果，那就太好了。让我们写一个脚本来完成这件事。

# 下面是程序要做的事：
# • 从命令行参数中获取查询关键字。
# • 取得查询结果页面。
# • 为每个结果打开一个浏览器选项卡。
# 这意味着代码需要完成以下工作：
# • 从 sys.argv 中读取命令行参数。
# • 用 requests 模块取得查询结果页面。
# • 找到每个查询结果的链接。
# • 调用 webbrowser.open()函数打开 Web 浏览器。
# 打开一个新的文件编辑器窗口，并保存为 lucky.py。

# 第１步：获取命令行参数，并请求查找页面
# 开始编码之前，你首先要知道查找结果页面的 URL。在进行 Google 查找后， 你
# 看浏览器地址栏，就会发现结果页面的 URL 类似于 https://www.google.com/
# search?q=SEARCH_TERM_HERE。 requests 模块可以下载这个页面，然后可以用
# Beautiful Soup，找到 HTML 中的查询结果的链接。最后，用 webbrowser 模块，在浏
# 览器选项卡中打开这些链接
import pyperclip
import requests, sys, webbrowser, bs4

print('Googling')  # display text while downloading the Google page

url = 'https://google.com/search?q=' + ' '.join(sys.argv[1:])
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
headers = {'user-agent': user_agent}
res = requests.get(url, headers=headers)
# webbrowser.open('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links
# 现在你需要使用 Beautiful Soup，从下载的 HTML 中，提取排名靠前的查找结果链
# 接。但如何知道完成这项工作需要怎样的选择器？例如，你不能只查找所有的<a>标
# 签， 因为在这个 HTML 中，有许多链接你是不关心的。因此，必须用浏览器的开发者
# 工具来检查这个查找结果页面，尝试寻找一个选择器，它将挑选出你想要的链接。
soup = bs4.BeautifulSoup(res.text, features='html.parser')
# linkElems = soup.select('.r a')
linkElems = soup.select('.yuRUbf a')

# TODO: Open a browser tab for each result.

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))
