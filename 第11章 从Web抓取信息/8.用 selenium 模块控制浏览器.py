# selenium 模块让 Python 直接控制浏览器，实际点击链接，填写登录信息，几乎
# 就像是有一个人类用户在与页面交互。与 Requests 和 Beautiful Soup 相比， Selenium
# 允许你用高级得多的方式与网页交互。但因为它启动了 Web 浏览器， 假如你只是想
# 从网络上下载一些文件，会有点慢，并且难以在后台运行。
# 附录 A 有安装第三方模块的详细步骤。

from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:\\Users\\admin\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe')
type(browser)  # <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')
