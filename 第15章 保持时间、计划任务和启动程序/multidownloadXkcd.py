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

import requests, os, bs4, threading

os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第15章 保持时间、计划任务和启动程序')
url = 'http://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print('Downloading page %s%s...' % (url, urlNumber))
        res = requests.get(url + str(urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if not comicElem:
            print('Could not find comic img')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
