#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   04.requests豆瓣电影.py
@Time    :   2023/05/25 15:27:27
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
dict = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20',
}
response = requests.get('https://movie.douban.com/j/chart/top_list?', params=dict, headers=headers)
object = response.json()
fp = open('./douban.json', 'w', encoding='utf-8')
json.dump(object, fp=fp, ensure_ascii=False)