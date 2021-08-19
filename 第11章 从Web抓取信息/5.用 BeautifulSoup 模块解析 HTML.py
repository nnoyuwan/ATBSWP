# Beautiful Soup 是一个模块，用于从 HTML 页面中提取信息（用于这个目的时，
# 它比正则表达式好很多）。 BeautifulSoup 模块的名称是 bs4（表示 Beautiful Soup，
# 第 4 版）。要安装它，需要在命令行中运行 pip install beautifulsoup4（关于安装第三
# 方模块的指导，请查看附录 A）。虽然安装时使用的名字是 beautifulsoup4，但要导
# 入它，就使用 import bs4。

# 11.5.1 从 HTML 创建一个 BeautifulSoup 对象
import os

import bs4
import requests

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features='html.parser')
type(noStarchSoup)  # <class 'bs4.BeautifulSoup'>
# 有了 BeautifulSoup 对象之后，就可以利用它的方法，定位 HTML 文档中的特定部分

# 11.5.2 用 select()方法寻找元素
# 表 11-2 举例展示了大多数常用 CSS 选择器的模式

# 传递给 select()方法的选择器                将匹配…
# soup.select('div')                    所有名为<div>的元素
# soup.select('#author')                带有 id 属性为 author 的元素
# soup.select('.notice')                所有使用 CSS class 属性名为 notice 的元素
# soup.select('div span')               所有在<div>元素之内的<span>元素
# soup.select('div > span')             所有直接在<div>元素之内的<span>元素， 中间没有其他元素
# soup.select('input[name]')            所有名为<input>，并有一个 name 属性，其值无所谓的元素
# soup.select('input[type="button"]')   所有名为<input>，并有一个 type 属性，其值为 button 的元素


import bs4, os

os.chdir('C:\\Users\\admin\\PycharmProjects\\ATBSWP\\第11章 从Web抓取信息')
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features='html.parser')
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()

str(elems[0])
print(elems[0].attrs)

# 这段代码将带有 id="author"的元素，从示例 HTML 中找出来。我们使用
# select('#author')返回一个列表，其中包含所有带有 id="author"的元素。
# 我们将这个 Tag 对象的列表保存在变量中 elems， len(elems)告诉我们列表中只有一个 Tag 对象，
# 只有一次匹配。在该元素上调用 getText()方法，返回该元素的文本，或内部的 HTML。
# 一个元素的文本是在开始和结束标签之间的内容：在这个例子中，就是'Al Sweigart'。

# 将该元素传递给 str()，这将返回一个字符串，其中包含开始和结束标签，以及该元
# 素的文本。最后， attrs 给了我们一个字典，包含该元素的属性'id'，以及 id 属性的值'author'。

# 也可以从 BeautifulSoup 对象中找出<p>元素。在交互式环境中输入以下代码：
pElems = exampleSoup.select('p')
import pprint

pprint.pprint(pElems)
pprint.pprint(len(pElems))  # 3
str(pElems[0])
# '<p>Download my <strong>Python</strong> book from <a href="http://\ninventwithpython.com">my website</a>.</p>'
pElems[0].getText()
# 'Download my Python book from my website.'
str(pElems[1])
# '<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()
# 'Learn Python the easy way!'
str(pElems[2])
# '<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText()

# 11.5.3 通过元素的属性获取数据
# Tag 对象的 get()方法让我们很容易从元素中获取属性值。向该方法传入一个属性名
# 称的字符串，它将返回该属性的值。利用 example.html，在交互式环境中输入以下代码：
soup = bs4.BeautifulSoup(open('example.html'), features='html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')
print(spanElem.get('some_nonexistent_addr') is None)
print(spanElem.attrs)

# 这里，我们使用 select()来寻找所有<span>元素，然后将第一个匹配的元素保存
# 在 spanElem 中。将属性名'id'传递给 get()，返回该属性的值'author'。
