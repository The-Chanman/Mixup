import sys
import Config
import requests
import time
import signal
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint


print 'A lookup of:', len(sys.argv), 'products.'
print 'Product List:', str(sys.argv)

productList = (sys.argv)
del productList[0]
print 'Product List:', productList

htmlProductFormat = []

for product in productList:
	htmlProductFormat.append(product.replace(" ", "%20"))

print htmlProductFormat[0]
url = 'https://www.amazon.com/s/&field-keywords='+htmlProductFormat[0]

driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)
#assert "Python" in driver.title
resultList = driver.find_elements_by_class_name("s-result-item")

# URLlist = []
f = open("result.txt","w") #opens file with name of "test.txt"
f.close()
f = open("result.txt","a")

for result in resultList:
	item = result.find_elements_by_class_name("a-link-normal")
	f.write(item[0].get_attribute('href')+"\n")
	# URLlist.append(item[0].get_attribute('href'))

f.close()
driver.close()
# firstItem = resultList[randint(0,9)].find_elements_by_class_name("a-link-normal")
# print firstItem[0].get_attribute('href')
