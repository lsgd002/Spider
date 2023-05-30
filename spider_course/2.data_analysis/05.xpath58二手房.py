#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   05.xpath.py
@Time    :   2023/05/29 15:52:53
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
response = requests.get(
    'https://tj.58.com/ershoufang/?from=esf&from=esf_list', headers=headers)
tree = etree.HTML(response.text, etree.HTMLParser(encoding='utf-8'))
file = open(r'spider_course\2.data_analysis\58wsf.txt', 'w', encoding='utf-8')
li_list = tree.xpath(
    '//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div')
for li in li_list:
    title = li.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
    quantity = li.xpath('./a/div[2]/div[2]/p[1]/span[1]/text()')
    unit = li.xpath('./a/div[2]/div[2]/p[1]/span[2]/text()')
    price = f'{quantity[0]}{unit[0]}'
    area = li.xpath('./a/div[2]/div[1]/section/div[1]/p[2]/text()')[0]
    print(title, price, area.strip())

    file.write(f'{title} {price} {area.strip()}' + '\n')
    