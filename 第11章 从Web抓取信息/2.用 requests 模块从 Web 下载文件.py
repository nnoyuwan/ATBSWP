# requests 模块让你很容易从 Web 下载文件，不必担心一些复杂的问题，诸如网
# 络错误、连接问题和数据压缩。 requests 模块不是 Python 自带的，所以必须先安装。
# 通过命令行，运行 pip install requests（附录 A 详细介绍了如何安装第三方模块）。

# 编写 requests 模块是因为 Python 的 urllib2 模块用起来太复杂。实际上，请拿一
# 支记号笔涂黑这一段。忘记我曾提到 urllib2。如果你需要从 Web 下载东西，使用
# requests 模块就好了。

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)

print(res.status_code)
print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

# 该 URL 指向一个文本页面，其中包含整部罗密欧与朱丽叶，它是由古登堡计
# 划提供的。通过检查 Response 对象的 status_code 属性，你可以了解对这个网页的
# 请求是否成功。如果该值等于 requests.codes.ok，那么一切都好（顺便说一下， HTTP
# 协议中“ OK”的状态码是 200。你可能已经熟悉 404 状态码，它表示“没找到”）。
# 如果请求成功，下载的页面就作为一个字符串，保存在 Response 对象的 text
# 变量中。这个变量保存了包含整部戏剧的一个大字符串，调用 len(res.text)表明，
# 它的长度超过 178000 个字符。最后，调用 print(res.text[:250])显示前 250 个字符。

# 11.2.2 检查错误
# 正如你看到的， Response 对象有一个 status_code 属性，可以检查它是否等于
# requests.codes.ok，了解下载是否成功。检查成功有一种简单的方法，就是在 Response
# 对象上调用 raise_for_status()方法。如果下载文件出错，这将抛出异常。如果下载成
# 功，就什么也不做。在交互式环境中输入以下代码：

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "C:\Users\admin\miniconda3\lib\site-packages\requests\models.py", line 941, in raise_for_status
#     raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist

# raise_for_status()方法是一种很好的方式，确保程序在下载失败时停止。这是一
# 件好事：你希望程序在发生未预期的错误时，马上停止。如果下载失败对程序来说
# 不够严重，可以用 try 和 except 语句将 raise_for_status()代码行包裹起来，处理这一
# 错误，不让程序崩溃。
