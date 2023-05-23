#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test2.py
@Time    :   2023/05/23 13:50:45
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

from utils import create_chrome_driver

browser = create_chrome_driver()
# browser.get('https://www.taobao.com/')
# browser.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbbb'})
browser.get('https://s.taobao.com/search?page=1&q=%E6%89%8B%E6%9C%BA')