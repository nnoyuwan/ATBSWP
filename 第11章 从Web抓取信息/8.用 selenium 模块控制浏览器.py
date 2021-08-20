# selenium 模块让 Python 直接控制浏览器，实际点击链接，填写登录信息，几乎
# 就像是有一个人类用户在与页面交互。与 Requests 和 Beautiful Soup 相比， Selenium
# 允许你用高级得多的方式与网页交互。但因为它启动了 Web 浏览器， 假如你只是想
# 从网络上下载一些文件，会有点慢，并且难以在后台运行。
# 附录 A 有安装第三方模块的详细步骤。

from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0')
browser = webdriver.Firefox(executable_path='C:\\Users\\admin\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe',
                            firefox_profile=profile)
# type(browser)  # <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
# browser.get('http://inventwithpython.com')

# 11.8.2 在页面中寻找元素
# WebDriver 对象有好几种方法，用于在页面中寻找元素。
# find_element_*方法返回一个 WebElement 对象，代表页面中
# 匹配查询的第一个元素。
# find_elements_*方法返回 WebElement_*对象的列表，包含
# 页面中所有匹配的元素。

# 表 11-3 selenium 的 WebDriver 方法，用于寻找元素
# 方法名                                             返回的 WebElement 对象/列表
# browser.find_element_by_class_name(name)
# browser.find_elements_by_class_name(name)         使用 CSS 类 name 的元素
# browser.find_element_by_css_selector(selector)
# browser.find_elements_by_css_selector(selector)   匹配 CSS selector 的元素
# browser.find_element_by_id(id)
# browser.find_elements_by_id(id)                   匹配 id 属性值的元素
# browser.find_element_by_link_text(text)
# browser.find_elements_by_link_text(text)          完全匹配提供的 text 的<a>元素
# browser.find_element_by_partial_link_text(text)
# browser.find_elements_by_partial_link_text(text)  包含提供的 text 的<a>元素
# browser.find_element_by_name(name)
# browser.find_elements_by_name(name)               匹配 name 属性值的元素
# browser.find_element_by_tag_name(name)
# browser.find_elements_by_tag_name(name)           匹配标签 name 的元素(大小写无关， <a>元素匹配'a'和'A')


# 表 11-4 WebElement 的属性和方法
# 属性或方法                  描述
# tag_name                  标签名，例如 'a'表示<a>元素
# get_attribute(name)       该元素 name 属性的值
# text                      该元素内的文本，例如<span>hello</span>中的'hello'
# clear()                   对于文本字段或文本区域元素，清除其中输入的文本
# is_displayed()            如果该元素可见，返回 True，否则返回 False
# is_enabled()              对于输入元素，如果该元素启用，返回 True，否则返回 False
# is_selected()             对于复选框或单选框元素，如果该元素被选中，选择 True，否则返回 False
# location                  一个字典，包含键'x'和'y'，表示该元素在页面上的位置

# try:
#     elem = browser.find_element_by_class_name('jumbotron')
#     print('Found <%s> element with that class name!' % elem.tag_name)
# except:
#     print('Was not able to find an element with that name.')

# 11.8.3 点击页面
# find_element_*和 find_elements_*方法返回的 WebElement 对象有一个 click()方法，
# 模拟鼠标在该元素上点击。这个方法可以用于链接跳转，选择单选按钮，点击提交按钮，
# 或者触发该元素被鼠标点击时发生的任何事情。例如，在交互式环境中输入以下代码：

# linkElem = browser.find_element_by_link_text('Read It Online')
# type(linkElem)
# linkElem.click()

# 11.8.4 填写并提交表单

# browser.get('http://gmail.com')
# emailElem = browser.find_element_by_id('identifierId')
# emailElem.send_keys('not_my_real_email@gmail.com')
# passwordElem = browser.find_element_by_id('Passwd')
# passwordElem.send_keys('12345')
# passwordElem.submit()

# 只要 Gmail 没有在本书出版后改变 Username 和 Password 文本字段的 id，上面的
# 代码就会用提供的文本填写这些文本字段（你总是可以用浏览器的开发者工具验证
# id）。在任何元素上调用 submit()方法，都等同于点击该元素所在表单的 Submit 按钮（你
# 可以很容易地调用 emailElem.submit()，代码所做的事情一样


# 11.8.5 发送特殊键
# selenium 有一个模块，针对不能用字符串值输入的键盘击键。它的功能非常类
# 似于转义字符。这些值保存在 selenium.webdriver.common.keys 模块的属性中。由于
# 这个模块名非常长，所以在程序顶部运行 from selenium.webdriver. common.keys import
# Keys 就比较容易。如果这么做，原来需要写 from selenium. webdriver.common.keys 的
# 地方，就只要写 Keys。表 11-5 列出了常用的 Keys 变量。


# 属性 含义
# Keys.DOWN, Keys.UP, Keys.LEFT,Keys.RIGHT 键盘箭头键
# Keys.ENTER, Keys.RETURN                  回车和换行键
# Keys.HOME, Keys.END,
# Keys.PAGE_DOWN,Keys.PAGE_UP              Home 键、 End 键、 PageUp 键和 Page Down 键
# Keys.ESCAPE, Keys.BACK_SPACE,Keys.DELETE Esc、 Backspace 和字母键
# Keys.F1, Keys.F2, . . . , Keys.F12       键盘顶部的 F1到 F12键
# Keys.TAB                                 Tab 键


# 例如，如果光标当前不在文本字段中，按下 home 和 end 键，将使浏览器滚动
# 到页面的顶部或底部。在交互式环境中输入以下代码，注意 send_keys()调用是如何
# 滚动页面的
from selenium.webdriver.common.keys import Keys

browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)  # scrolls to bottom
# htmlElem.send_keys(Keys.HOME)  # scrolls to top

# 11.8.6 点击浏览器按钮
# 利用以下的方法， selenium 也可以模拟点击各种浏览器按钮：
# browser.back()点击“返回”按钮
# browser.forward()点击“前进”按钮。
# browser.refresh()点击“刷新”按钮。
# browser.quit()点击“关闭窗口”按钮。

# 11.8.7 关于 selenium 的更多信息
# selenium 能做的事远远超出了这里描述的功能。它可以修改浏览器的 cookie，
# 截取页面快照， 运行定制的 JavaScript。要了解这些功能的更多信息，请参考文档：
# http://selenium-python.readthedocs.org/。


