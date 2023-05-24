#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2023/05/22 16:41:44
@Author  :   jumploop 
@Version :   1.0
@Desc    :   因为淘宝网的搜索功能需要登录后才能使用，所以我们需要通过程序去控制浏览器实现登录功能，然后再获取登录后的cookie。
             首先创建一个Chrome浏览器对象，用这个对象去操控浏览器。
'''

import json
from selenium import webdriver



# 创建谷歌浏览器对象，用selenium控制浏览器访问url
def create_chrome_driver(*, headless=False):
    options = webdriver.ChromeOptions()
    if headless:  # 如果为True，则爬取时不显示浏览器窗口
        options.add_argument('--headless')

    # 做一些控制上的优化
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 创建浏览器对象
    browser = webdriver.Chrome(
        options=options, executable_path=r'C:\Users\wdl\Spider\taobao_spider\chromedriver.exe')
    # 破解反爬措施
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )

    return browser

def add_cookies(browser, cookies_file):
    """添加指定cookie到浏览器"""
    with open(cookies_file, 'r') as f:
        cookies_list = json.load(f)
        for cookie_dict in cookies_list:
            if cookie_dict['secure']:
                browser.add_cookie(cookie_dict)