# 博客和其他经常更新的网站通常有一个首页，其中有最新的帖子，以及一个“前
# 一篇”按钮，将你带到以前的帖子。然后那个帖子也有一个“前一篇”按钮，以此
# 类推。这创建了一条线索，从最近的页面，直到该网站的第一个帖子。如果你希望
# 拷贝该网站的内容，在离线的时候阅读，可以手工导航至每个页面并保存。但这是
# 很无聊的工作，所以让我们写一个程序来做这件事。


# XKCD 是一个流行的极客漫画网站，它符合这个结构（参见图 11-6）。首页
# http://xkcd.com/有一个“ Prev”按钮，让用户导航到前面的漫画。手工下载每张漫
# 画要花较长的时间，但你可以写一个脚本，在几分钟内完成这件事

# 下面是程序要做的事：
# • 加载主页；
# • 保存该页的漫画图片；
# • 转入前一张漫画的链接；
# • 重复直到第一张漫画。

import requests, os, bs4

os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第11章 从Web抓取信息')
url = 'http://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):

    # download the page.
    print('Download page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
print('Done')
# 有一些 XKCD 页面有特殊的内容，不是一个简单的图像文件。这没问题，跳过它们
# 就好了。如果选择器没有找到任何元素，那么 soup.select('#comic img')将返回一个空的列
# 表。出现这种情况时，程序将打印一条错误消息，不下载图像，继续执行。
# 否则，选择器将返回一个列表，包含一个<img>元素。可以从这个<img>元素中
# 取得 src 属性，将它传递给 requests.get()，下载这个漫画的图像文件。
