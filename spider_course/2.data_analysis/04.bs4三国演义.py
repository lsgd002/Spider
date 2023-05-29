#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   04.bs4三国演义.py
@Time    :   2023/05/29 14:37:51
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
response = requests.get(
    'https://www.shicimingju.com/book/sanguoyanyi.html', headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
li_list = soup.select("div.book-mulu li")
file = open(r'spider_course\2.data_analysis\sanguo.txt', 'w', encoding='utf-8')
for li in li_list:
    title = li.a.text
    detail_url = 'https://www.shicimingju.com' + li.a['href']
    detail_response = requests.get(detail_url, headers=headers)
    detail_response.encoding = 'utf-8'
    detail_soup = BeautifulSoup(detail_response.text, 'lxml')
    div_tag = detail_soup.select_one('div.chapter_content')
    content = div_tag.text
    file.write(title + '\n' + content + '\n')
    print(title + ' 爬取成功')
