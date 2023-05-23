#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   taobao.py
@Time    :   2023/05/22 16:45:31
@Author  :   lsgd002 
@Version :   1.0
@Desc    :   https://www.bilibili.com/video/BV1QY411F7Vt?p=12
             https://blog.csdn.net/qq_47188967/article/details/125421176
'''


import scrapy
from scrapy import Selector
from taobao_spider.items import TaobaoSpiderItem

from scrapy.spiders import Spider


class TaobaoSpider(Spider):
    name = "taobao"
    allowed_domains = ["www.taobao.com"]
    start_urls = [
        "https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&q=%E6%89%8B%E6%9C%BA"]

    def parse(self, response):
        for item in Selector(response).css('div.Content--content--sgSCZ12 > div'):
            taobaoitem = TaobaoSpiderItem()
            taobaoitem['title'] = item.css(
                'div.Title--descWrapper--HqxzYq0 > div > span::text').get()
            price_int = item.css('span.Price--priceInt--ZlsSi_M::text').get()
            price_float = item.css(
                'span.Price--priceFloat--h2RR0RK::text').get()
            taobaoitem['price'] = f'￥{price_int.strip()}.{price_float.strip()}' if price_int and price_float else None
            taobaoitem['deal_count'] = item.css(
                'span.Price--realSales--FhTZc7U::text').get()
            taobaoitem['shop_name'] = item.css(
                'div.ShopInfo--TextAndPic--yH0AZfx > a::text').get()
            taobaoitem['shop_location'] = item.css(
                'div.Price--priceWrapper--Q0Dn7pN > div:nth-child(5) > span::text').get()
            yield taobaoitem


