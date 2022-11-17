import scrapy
import requests
from scrapy import Selector

url="https://datacell.netlify.app/"
html=requests.get(url).content
#print(html)
sel=Selector(text=html)
#xpath='/html/head/title/text()'
xpath='//a/@href'
titlte1=sel.xpath(xpath).get()

print(titlte1)


