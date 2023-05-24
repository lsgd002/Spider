#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   requests_01.py
@Time    :   2023/05/24 20:36:53
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
from bs4 import BeautifulSoup

# 发送请求
response = requests.get('https://www.sogou.com/')
# 获取响应数据
page_text = response.text


# # 解析数据
soup = BeautifulSoup(page_text, features='html.parser')
# # 格式化数据
page_text = soup.prettify()

# 输出数据
print(page_text)
with open('./sogou.txt', 'w', encoding='utf-8') as f:
    f.write(page_text)
print('爬取完毕！')