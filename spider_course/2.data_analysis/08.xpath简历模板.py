#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   08.xpath简历模板.py
@Time    :   2023/05/30 15:58:37
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
response = requests.get(
    'https://sc.chinaz.com/jianli/free.html', headers=headers)
response.encoding = 'utf-8'
tree = etree.HTML(response.text, etree.HTMLParser(encoding='utf-8'))

path = r'spider_course\2.data_analysis\简历模板'
if not os.path.exists(path=path):
    os.mkdir(path=path)

resume_template_list = tree.xpath('//*[@id="container"]/div')

for resume_template in resume_template_list:
    resume_template_name = resume_template.xpath('./a/img/@alt')[0]
    resume_template_url = resume_template.xpath('./a/@href')[0]

    response_download = requests.get(resume_template_url, headers=headers)
    response_download.encoding = 'utf-8'
    tree_download = etree.HTML(
        response_download.text, etree.HTMLParser(encoding='utf-8'))
    resume_template_download_list = tree_download.xpath(
        '//*[@id="down"]/div[2]/ul/li[1]')

    for download_list in resume_template_download_list:
        download_url = download_list.xpath('./a/@href')[0]
        response = requests.get(download_url, headers=headers).content

        with open(f'{path}/{resume_template_name}.rar', 'wb') as f:
            f.write(response)

        print(f'{resume_template_name}下载成功！')
