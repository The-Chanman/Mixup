import sys
import requests
import time
import signal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


print 'A lookup of:', len(sys.argv), 'products.'
print 'Product List:', str(sys.argv)

productList = (sys.argv)
del productList[0]
print 'Product List:', productList

htmlProductFormat = []

for product in productList:
	htmlProductFormat.append(product.replace(" ", "-"))

print htmlProductFormat[0]
url = 'https://canopy.co/shop/'+htmlProductFormat[0]

driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)
#assert "Python" in driver.title
elem = driver.find_elements_by_class_name("price")
print elem[0].text
# elem.clear()
# elem.send_keys("echan@ideo.com")

# elem = driver.find_element_by_name("password")
# print(elem)
# elem.clear()
# elem.send_keys("ch52690")

# elem.send_keys(Keys.RETURN)

# time.sleep(10)

# elem = driver.find_elements_by_class_name("triggers_entry")
# elem[0].clear()
# elem[0].send_keys("awesome")
# elem[1].clear()
# elem[1].send_keys("amazing")
# elem[2].clear()
# elem[2].send_keys("history")

# elem = driver.find_elements_by_class_name("responses_entry")
# elem[0].clear()
# elem[0].send_keys("Yeah! That's awesome! (Almost as awesome as the IDEO core Team!)")
# elem[1].clear()
# elem[1].send_keys("Wow that's AMAZING! (Almost as amazing as team Glowy Recs - nice try Joel)")
# elem[2].clear()
# elem[2].send_keys("I'm busy making history instead of reading about it.  -Chanman")

# time.sleep(5)
# elem = driver.find_elements_by_class_name("save_response_button")
# elem[0].click()
# elem[1].click()
# elem[2].click()

# driver.close()
