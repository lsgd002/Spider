#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   06.xpath壁纸.py
@Time    :   2023/05/30 13:49:22
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
response = requests.get('https://pic.netbian.com/4kmeinv/', headers=headers)
response.encoding = 'gbk'
tree = etree.HTML(response.text, etree.HTMLParser(encoding='utf-8'))
li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')

if not os.path.exists(r'spider_course\2.data_analysis\picture'):
    os.mkdir(r'spider_course\2.data_analysis\picture')

for li in li_list:
    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    img = li.xpath('./a/img/@src')[0]
    img_url = 'https://pic.netbian.com' + img

    img_response = requests.get(img_url, headers=headers)
    img_path = r'C:\Users\wdl\Spider\spider_course\2.data_analysis\picture\\'  # 图片保存路径
    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'  # 获取图片名称
    img_response = requests.get(img_url, headers=headers)
    with open(img_path + img_name, 'wb') as file:
        file.write(img_response.content)
    