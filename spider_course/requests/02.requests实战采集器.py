#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   02.requests实战采集器.py
@Time    :   2023/05/25 14:04:12
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
from bs4 import BeautifulSoup

# 伪装浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
}
# 发送请求
keyword = input('请输入要搜索的关键字：')
params = {'params': keyword}
response = requests.get('https://www.sogou.com/web', params=params, headers=headers)
# 获取响应数据
page_text = response.text
soup = BeautifulSoup(page_text, features='html.parser')
# 格式化数据
soup = soup.prettify()
# 输出数据
print(soup)
# 持久化
with open(f'./{keyword}.html', 'w', encoding='utf-8') as f:
    f.write(soup)