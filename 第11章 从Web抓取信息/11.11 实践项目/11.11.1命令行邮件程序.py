

from selenium import webdriver

path = 'C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=path)
get = chrome.get('https://mail.qq.com/')

u = chrome.find_element_by_id('loginform')
# attribute = u.get_attribute('value')
# print(attribute)
u.send_keys('509194515')
# p = chrome.find_element_by_id('p')
# p.send_keys('123Jiangyan.')
