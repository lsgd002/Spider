#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   02.360img.py
@Time    :   2023/05/26 15:23:44
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50' 
}

page_text = requests.get('https://www.sohu.com/a/35074007_130784', headers=header).text

with open('./360img.text', 'w', encoding='utf-8') as fp:
    fp.write(page_text)

"""
<p><img alt="" src="http://photocdn.sohu.com/20151011/mp35074007_1444545045074_1.gif"></p>
<p><img alt="" data-src="24hzZPxRzhaza9Jxy//c7ThQgnKmvl7gI3CnHj0mlvRS/pQZDT6Mya3jE+Y9K1IDUrs/GVB6pK6o8Mx1EuJ1i9Ve/jleNpUW7jTcl0e14d0=" /></p>
"""
ex = '<p><img alt="" data-src="24hzZPxRzhaza9Jxy//c7ThQgnKmvl7gI3CnHj0mlvRS/pQZDT6Mya3jE+Y9K1IDOUNMy2dIfapquLST61GjONVe/jleNpUW7jTcl0e14d0=" /></p> '
img_src_list = re.findall(ex, page_text, re.S)
print(img_src_list)