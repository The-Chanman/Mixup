import sys
import Config
import requests
import time
import signal
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

valid = {"yes": True, "y": True, "ye": True, "sure": True, "nah": False, "yeah": True, "good": True, "bad": False, "meh": False, "no": False, "n": False}

def lookup(perferences):
	htmlProductFormat = []
	for product in productList:
		htmlProductFormat.append(product.replace(" ", "%20"))

	url = 'https://www.amazon.com/s/&field-keywords='+htmlProductFormat[0]+ " " +perferences.replace(" ", "%20")

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

	firstItem = resultList[randint(0,15)].find_elements_by_class_name("a-link-normal")
	driver.get(firstItem[0].get_attribute('href')) 

# driver.close()

productList = (sys.argv)
del productList[0]
print 'Orpheus: Hey Becca would you like to restock on your ' + productList[0] + ". I know you're a big fan of coffee."
response = raw_input("How about it? ")
if response.lower() in valid and valid[response.lower()]:
	if valid[response.lower()]:
		preferences = raw_input('Orpheus: Any preferences? A dark roast perhaps? Caffineated? ')
		if not(preferences.lower() in valid):
			lookup(preferences)
		else:
			print 'Orpheus: Generic it is.'
			lookup('')
	else:
		print 'Orpheus: Okay we won\'t restock then'
else:
	print 'Orpheus: Okay we won\'t restock then'




