#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   05.requests肯德基餐厅位置.py
@Time    :   2023/05/25 15:58:46
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
from bs4 import BeautifulSoup
import json

# 伪装浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
    }

keyword = input('请输入要搜索的地点：')
data = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': '1',
    'pageSize': '10',
}
# 获取餐厅位置
response = requests.post('http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?',data=data['keyword'], headers=headers)

page_text = response.text

with open('./kfc.txt', 'w', encoding='utf-8') as file:
    file.write(page_text)


