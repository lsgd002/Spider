import scrapy
import re

from spider2023.items import MovieItem
from scrapy import Selector, Request
from scrapy.http import HtmlResponse


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    
    def start_requests(self):
        for i in range(1):
            yield Request(url=f'https://movie.douban.com/top250?start={i * 25}&filter=')

    def parse(self, response, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            detail_url = list_item.css('div.info > div.hd > a::attr(href)').extract_first()
            movie_item = MovieItem()
            movie_item['title'] = list_item.css('span.title::text').extract_first()
            movie_item['rank'] = list_item.css('span.rating_num::text').extract_first()
            movie_item['subject'] = list_item.css('span.inq::text').extract_first()
            yield Request(url=detail_url, callback=self.parse_detail, cb_kwargs={'item': movie_item})

        # href_items = sel.css('div.paginator > a::attr(href)')
        # for href_item in href_items:
        #     yield Request(url=response.urljoin(href_item.extract()))

    # def parse_detail(self, response, **kwarge):
    #     movie_item = kwarge['item']
    #     sel = Selector(response)
    #     movie_item['duration'] = sel.css('span[property="v:runtime"]::text').extract_first()
    #     # 获取剧情简介展开全部链接的 URL
    #     expand_url = sel.css('#link-report-intra > span.short > a::attr(href)').extract_first()
    #     movie_item['intro'] = sel.css('span[property="v:summary"]::text').extract_first()
    #     # 正则表达式替换intro中的换行符
    #     movie_item['intro'] = re.sub(r'\s+', '', movie_item['intro'])
    #     yield movie_item

    def parse_detail(self, response, **kwargs):
        movie_item = kwargs['item']
        sel = Selector(response)
        movie_item['duration'] = sel.css('span[property="v:runtime"]::text').extract_first()
        
        # 提取剧情简介展开全部的JavaScript代码
        script_text = response.css('#link-report-intra > span.short > a::attr(href)').extract_first()
        expand_url = re.search(r'"(https?://.*?)"', script_text)
        if expand_url:
            expand_url = expand_url.group(1)
            yield Request(url=expand_url, callback=self.parse_expand, cb_kwargs={'item': movie_item})

    def parse_expand(self, response, **kwargs):
        movie_item = kwargs['item']
        sel = Selector(response)
        movie_item['intro'] = sel.css('div#link-report span[property="v:summary"]::text').extract_first()
        # 正则表达式替换intro中的换行符
        movie_item['intro'] = re.sub(r'\s+', '', movie_item['intro'])
        yield movie_item






