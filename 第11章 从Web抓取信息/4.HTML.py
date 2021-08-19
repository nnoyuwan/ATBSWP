# 在你拆解网页之前，需要学习一些 HTML 的基本知识。你也会看到如何利用
# Web 浏览器的强大开发者工具，它们使得从 Web 抓取信息更容易。


# 11.4.1 学习 HTML 的资源
# 超文本标记语言（ HTML）是编写 Web 页面的格式。本章假定你对 HTML 有
# 一些基本经验，但如果你需要初学者指南，我推荐以下站点：
# • http://htmldog.com/guides/html/beginner/
# • http://www.codecademy.com/tracks/web/
# • https://developer.mozilla.org/en-US/learn/html/


# 11.4.2 快速复习
# 假定你有一段时间没有看过 HTML 了，这里是对基本知识的快速复习。 HTML
# 文件是一个纯文本文件，带有.html 文件扩展名。这种文件中的文本被“标签”环绕，
# 标签是尖括号包围的单词。标签告诉浏览器以怎样的格式显示该页面。一个开始标
# 签和一个结束标签可以包围某段文本，形成一个“元素”。“文本”（或“内部的HTML”）是在开始标签和结束标签之间的内容。例如，下面的 HTML 在浏览器中
# 显示 Hello world!，其中 Hello 用粗体显示。

# <strong>Hello</strong> world!

# 开始标签<strong>表明，标签包围的文本将使用粗体。结束标签</strong>告诉
# 浏览器，粗体文本到此结束。

# HTML 中有许多不同的标签。有一些标签具有额外的特性，在尖括号内以“属
# 性”的方式展现。例如， <a>标签包含一段文本，它应该是一个链接。这段文本链
# 接的 URL 是由 href 属性确定的。下面是一个例子：

# Al's free <a href="http://inventwithpython.com">Python books</a>.

# 某些元素具有 id 属性，可以用来在页面上唯一地确定该元素。你常常会告诉程
# 序，根据元素的 id 属性来寻找它。所以利用浏览器的开发者工具，弄清楚元素的 id
# 属性，这是编写 Web 抓取程序常见的任务


# 11.4.3 查看网页的 HTML 源代码
# 在浏览器的任意网页上点击右键（或在 OS X 上 Ctrl-点击），选择 View Source 或 View page
# source。

# 11.4.4 打开浏览器的开发者工具
# Chrome：Win -- F12, OS X -- Cmd-Option-I
# Firefox：Win，Linux --  Ctrl-Shift-C, OS X -- Cmd-Option-C
# Safari：打开 Preferences 窗口，并在 Advanced pane 选中 Show Develop menu in the menu bar 选项。在它启用后，你可以按下 Cmd-option-I

# 不要用正则表达式来解析 HTML
# 在一个字符串中定位特定的一段 HTML，这似乎很适合使用正则表达式。但
# 是，我建议你不要这么做。 HTML 的格式可以有许多不同的方式，并且仍然被认
# 为是有效的 HTML，但尝试用正则表达式来捕捉所有这些可能的变化，将非常繁
# 琐，并且容易出错。专门用于解析 HTML 的模块，诸如 Beautiful Soup， 将更不容
# 易导致缺陷。在 http://stackoverflow.com/a/1732454/1893164/，你会看到更充分的
# 讨论，了解为什么不应该用正则表达式来解析 HTML。


# 11.4.5 使用开发者工具来寻找 HTML 元素
# 程序利用 requests 模块下载了一个网页之后，你会得到该页的 HTML 内容，作为一
# 个字符串值。现在你需要弄清楚，这段 HTML 的哪个部分对应于网页上你感兴趣的信息。
# 这就是可以利用浏览器的开发者工具的地方。假定你需要编写一个程序，从
# http://weather.gov/获取天气预报数据。在写代码之前，先做一点调查。如果你访问该网
# 站，并查找邮政编码 94105，该网站将打开一个页面，显示该地区的天气预报。

# <p class="myforecast-current-lrg">64°F</p>

# 通过开发者工具，可以看到网页中负责气温部分的 HTML是<p class= "myforecastcurrent-lrg">57°F</p>。这正是你要找的东西！看起来气温信息包含在一个<p>元素
# 中， 带有 myforecast-current-lrg 类。既然你知道了要找的是什么， BeautifulSoup 模
# 块就可以帮助你在这个字符串中找到它。
