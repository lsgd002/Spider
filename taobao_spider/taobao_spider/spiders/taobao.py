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


class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["www.taobao.com"]

    def start_requests(self):
        keywords = ['手机']
        for keyword in keywords:
            for page in range(1):
                url = f'https://s.taobao.com/search?q={keyword}&s={48 * page}'
                yield scrapy.Request(url=url)

    # def parse(self, response):
    #     for item in Selector(response).css('div.Content--content--sgSCZ12 > div > div > a > div.Card--doubleCard--wznk5U4'):
    #         taobaoitem = TaobaoSpiderItem()
    #         # taobaoitem['title'] = item.css(
    #         #     'div.Title--descWrapper--HqxzYq0 > div > span::text').extract_first()
    #         # price_int = item.css(
    #         #     'span.Price--priceInt--ZlsSi_M::text').extract_first()
    #         # price_float = item.css(
    #         #     'span.Price--priceFloat--h2RR0RK::text').extract_first()
    #         # taobaoitem['price'] = f'￥{price_int.strip()}.{price_float.strip()}' if price_int and price_float else None
    #         taobaoitem['deal_count'] = item.css(
    #             'a > div > div.Card--mainPicAndDesc--wvcDXaK.gwd-item > div.Price--priceWrapper--Q0Dn7pN > span.Price--realSales--FhTZc7U::text').extract_first()
    #         taobaoitem['shop_name'] = item.css(
    #             'a.ShopInfo--shopName--rg6mGmy::text').extract_first()
    #         taobaoitem['shop_location'] = item.css(
    #             'div.Price--priceWrapper--Q0Dn7pN > div:nth-child(5) > span::text').extract_first()
    #         yield taobaoitem

    def parse(self, response, **kwargs):  # 淘宝的数据是通过js动态渲染出来的，不是静态内容，通过选择器拿不到，我们要通过selenium帮助我们拿到,在数据管道中实现
            sel = Selector(response)
            selectors = sel.css('div.Content--content--sgSCZ12 > div.Content--contentInner--QVTcU0M > div > a.Card--doubleCardWrapper--L2XFE73 > div.Card--doubleCard--wznk5U4')
            for selector in selectors:  
                item = TaobaoSpiderItem()
                item['title'] = ''.join(selector.css('div.Card--mainPicAndDesc--wvcDXaK.gwd-item > div.Title--descWrapper--HqxzYq0 > div > span::text').extract())
                item['price'] = selector.css('div.Card--mainPicAndDesc--wvcDXaK.gwd-item > div.Price--priceWrapper--Q0Dn7pN > span.Price--priceInt--ZlsSi_M::text').extract_first()
                item['deal_count'] = selector.css('div.Card--mainPicAndDesc--wvcDXaK.gwd-item > div.Price--priceWrapper--Q0Dn7pN > span.Price--realSales--FhTZc7U::text').extract_first()
                item['shop'] = selector.css('div.ShopInfo--shopInfo--ORFs6rK > div.ShopInfo--TextAndPic--yH0AZfx > a::text').extract_first()
                item['location'] = selector.css('div.Card--mainPicAndDesc--wvcDXaK.gwd-item > div.Price--priceWrapper--Q0Dn7pN > div:nth-child(5) > span::text').extract_first()
                yield item
