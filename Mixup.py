from lxml import html
import sys
import requests

print 'A lookup of:', len(sys.argv), 'products.'
print 'Product List:', str(sys.argv)

productList = (sys.argv)
del productList[0]
print 'Product List:', productList

htmlProductFormat = []

for product in productList:
	htmlProductFormat.append(product.replace(" ", "-"))

print htmlProductFormat

page = requests.get('https://www.amazon.com/s/&field-keywords=', htmlProductFormat[0])
print page

tree = html.fromstring(page.content)

productOptions = tree.xpath('//div[@id="atfResults"]')
print productOptions