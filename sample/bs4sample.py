# coding: utf-8
from bs4 import BeautifulSoup as soup
html = '<span class="price">￥929</span>'
doc = soup(html, "lxml")
print(doc.find("span", class_="price").string)