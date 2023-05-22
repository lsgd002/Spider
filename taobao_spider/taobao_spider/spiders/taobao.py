import scrapy
from scrapy import Selector
from taobao_spider.items import TaobaoSpiderItem


class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["www.taobao.com"]
    start_urls = ["https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&q=%E6%89%8B%E6%9C%BA"]

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css('div.Content--content--sgSCZ12 > div')
        for item in list_items:
            taobaoitem = TaobaoSpiderItem()
            taobaoitem['title'] = item.css('div.Title--descWrapper--HqxzYq0 > div > span::text').extract_first().strip()
            taobaoitem['price'] = item.css('div.Price--priceWrapper--Q0Dn7pN > span.Price--priceInt--ZlsSi_M::text').extract_first().strip()
            taobaoitem['price'] = taobaoitem['price'].join(['￥', item.css('span.Price--priceFloat--h2RR0RK::text').extract_first().strip()])
            taobaoitem['deal_count'] = item.css('span.Price--realSales--FhTZc7U::text').extract_first().strip()
            taobaoitem['shop_name'] = item.css('div.ShopInfo--TextAndPic--yH0AZfx > a::text').extract_first().strip()
            taobaoitem['shop_location'] = item.css('div.Price--priceWrapper--Q0Dn7pN > div:nth-child(5) > span::text').extract_first().strip()
            yield taobaoitem
