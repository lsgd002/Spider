# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class Spider2023Pipeline:

    def __init__(self) -> None:
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'doubanTop250'
        self.ws.append(['电影名称', '评分', '主题', '时长', '简介'])

    def close_spider(self, spider):
        self.wb.save('doubanTop250.xlsx')

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        duration = item.get('duration', '')
        intro = item.get('intro', '')
        self.ws.append((title, rank, subject, duration, intro))
        return item
