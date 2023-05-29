import requests
from bs4 import BeautifulSoup
import chardet
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
response = requests.get('https://guangdiu.com/search.php?q=%E4%B8%89%E5%85%83%E6%9E%81%E8%87%B4&keyfrom=hsearch', headers=headers)
html = response.text
tree = etree.HTML(html)
for text in tree.xpath("//a[@class='goodname']/text()"):
    soup = BeautifulSoup(html, 'html.parser')
    for text in soup.select("a.goodname"):
        print(text.get_text(strip=True))


