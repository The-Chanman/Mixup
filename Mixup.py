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

print htmlProductFormat[0]
print 'https://canopy.co/shop/'+htmlProductFormat[0]
page = requests.get('https://canopy.co/shop/'+htmlProductFormat[0])
print page.content

tree = html.fromstring(page.content)
print tree

productOptions = tree.xpath('//div[@class="product-details-name"]/text()')
print productOptions