import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

path = 'C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=path)
browser = chrome.get('https://gabrielecirulli.github.io/2048/')

keys = [Keys.DOWN, Keys.RIGHT]
while True:
    i = randint(0, 1)
    print(i)
    key = keys[i]
    htmlElem = chrome.find_element_by_tag_name('html')
    htmlElem.send_keys(key)
    time.sleep(0.2)
