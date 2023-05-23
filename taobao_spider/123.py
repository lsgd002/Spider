from selenium.webdriver.edge.service import Service
from selenium import webdriver
import time
 
 
# 创建浏览器操作对象
browser = webdriver.Edge(service=Service(r'C:\Users\wdl\Spider\taobao_spider\msedgedriver.exe'))

 
# 获取前端页面
browser.get('http://www.baidu.com')
 
 
print('浏览器已打开')
