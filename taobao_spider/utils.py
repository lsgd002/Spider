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
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
 
 

#无perform，只点击但不执行函数行为；有perform，则会执行函数
def create_chrome_driver(*, headless=False):  # 创建谷歌浏览器对象，用selenium控制浏览器访问url
    options = webdriver.EdgeOptions()
    if headless:  # 如果为True，则爬取时不显示浏览器窗口
        options.add_argument('--headless')

    # 做一些控制上的优化
    options.set_capability('ms:edgeOptions', {'sync': False}) 
    options.add_argument('--disable-features=msEdge.Sync')
    options.set_capability('ms:edgeOptions', {'useAutomationExtension': False})
    options.set_capability('ms:edgeOptions', {'profile': {'default_content_setting_values': {'cookies': 2}}})
    options.set_capability('ms:edgeOptions', {'excludeSwitches': ['enable-automation']})


    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 创建浏览器对象
    browser = webdriver.Edge(options=options,service=Service(r'C:\Users\wdl\Spider\taobao_spider\msedgedriver.exe'))
    # 破解反爬措施
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )

    return browser
