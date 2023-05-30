#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   07.xpath全国城市名称.py
@Time    :   2023/05/30 14:37:12
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
response = requests.get('https://www.aqistudy.cn/historydata/', headers=headers)
response.encoding = 'utf-8'
tree = etree.HTML(response.text, etree.HTMLParser(encoding='utf-8'))
# 一次性解析所有城市
all_city_names = []
all_city_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
for all_city in all_city_list:
    all_city_name = all_city.xpath('./text()')[0]
    all_city_names.append(all_city_name)

print(all_city_names, len(all_city_names))
