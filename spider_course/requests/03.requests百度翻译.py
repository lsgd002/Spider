#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   03.requests百度翻译.py
@Time    :   2023/05/25 14:27:17
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

# 发送请求
keyword = input('请输入要翻译的内容：')
data = {
    'kw': keyword
}
response = requests.post(
    url='https://fanyi.baidu.com/sug', data=data, headers=headers)
# 获取响应数据
dict_obj = response.json()
# 格式化数据
# ensure_ascii=False: 不使用ascii码, indent=4: 缩进4个空格
fp = open(f'./{keyword}.json', 'w', encoding='utf-8')
json_str = json.dump(dict_obj, fp=fp, ensure_ascii=False, indent=4)
