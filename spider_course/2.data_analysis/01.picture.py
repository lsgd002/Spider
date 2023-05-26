#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   01.picture.py
@Time    :   2023/05/26 15:16:23
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   None
'''

import requests
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50' 
}

img_data = requests.get('https://p0.ssl.qhimgs1.com/sdr/400__/t019c9b83248dac91ca.jpg', headers=header).content

with open('./meinv.jpg', 'wb') as fp:
    fp.write(img_data)