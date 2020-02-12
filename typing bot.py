# Importing required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Opening website
chrome = webdriver.Chrome()
chrome.get('https://www.livechatinc.com/typing-speed-test/#/')

#Wait while website opens
chrome.implicitly_wait(5)

#Set timeout time for while loop. 60 seconds.
timeout = time.time() + 60

#Grab current word to type and then enter it. Stop after 60 seconds.
while True:
    if time.time() > timeout:
        break
    else:
        string = ''
        counter = 0
        while '<' not in string:
            string += chrome.page_source[chrome.page_source.index('data-reactid=".0.2.0.0.$=12.0.$=10.1.0.$0"')+43+counter]
            counter += 1
        string = string.replace('<',' ')
        action = ActionChains(chrome)
        action.send_keys(string)
        action.perform()