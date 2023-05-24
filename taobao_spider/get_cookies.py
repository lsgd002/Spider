#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2023/05/24 13:55:33
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import json
import time

from create_chrome import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


browser = create_chrome_driver()
browser.get('https://login.taobao.com/')

# 隐式等待
browser.implicitly_wait(10)

# 获取页面元素模拟用户输出和点击行为
username_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-id')
username_input.send_keys('lsgd002') # 填写用户名

password_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-password')
password_input.send_keys('long13gotk23meng') # 填写密码

# 登录按钮
login_button = browser.find_element(By.CSS_SELECTOR, '#login-form > div.fm-btn > button')
login_button.click()

# 显式等待
# wait_obj = WebDriverWait(browser, 10)
# wait_obj.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.m-userinfo')))
time.sleep(10)

# 获取登录后的cookie，并写入文件
with open('taobao.json', 'w') as f:
    json.dump(browser.get_cookies(), f)