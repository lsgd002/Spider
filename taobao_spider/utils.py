#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2023/05/22 16:41:44
@Author  :   jumploop 
@Version :   1.0
@Desc    :   因为TB网的搜索功能需要登录之后才能使用，所以我们要通过程序去控制浏览器实现登录功能，然后再获取登录之后的Cookie.
             首先创建一个Chrome浏览器对象，用这个对象去操控谷歌浏览器：
'''

import json
from selenium import webdriver


def creat_chrom_driver(): # 创建一个Chrome浏览器对象,用selenuim去控制谷歌浏览器
    options = webdriver.ChromeOptions()
    if headless: # 如果headless为True,则无界面运行
        options.add_argument('--headless')
        
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    return driver