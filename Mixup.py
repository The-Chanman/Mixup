from lxml import html
import sys
import requests

print 'A lookup of:', len(sys.argv), 'products.'
print 'Product List:', str(sys.argv)

productList = str(sys.argv)

for product in productList:
	product.replace(" ", "-")

print productList