import time
from selenium import webdriver
import urllib.request as req
import requests
# import wget


print("What you want to search")
searchImg = input()
driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
#Opens with bing search engine with Animals search
Search = "https://www.bing.com/images/search?scenario=ImageBasicHover&cw=1349&ch=646&q="+searchImg +"&first=1"
driver.get(Search)
time.sleep(3)
#Clicks on the filter
driver.find_element_by_class_name("fltIdtTit").click()
time.sleep(3)
#Clicks on the License Filter
driver.find_element_by_xpath("//span[@title='License filter']").click()
time.sleep(3)


#Selects the Free to share and use options from the dropdown.
driver.find_element_by_xpath("//span[text() = 'Free to share and use commercially']").click()
time.sleep(3)
#clicks on the first image
driver.find_element_by_class_name("mimg").click()
#As the page changes the url is loaded to the ImageUrl variable
ImageUrl = driver.current_url
# Catches the image page
driver.get(ImageUrl)
time.sleep(3)
for i in range(0,100):
	#selects the src of the image i.e., url
	imagesource= driver.find_element_by_xpath("//*[@id='mainImageWindow']/div[1]/div/div/div/img").get_attribute("src")
	time.sleep(4)
	print(imagesource)
	
	li = imagesource.split('/')
	name = li[-1]
	li1 = name.split("?")
	if (len(li1) == 1):
		req.urlretrieve(imagesource, name)
	else:
		req.urlretrieve(imagesource, li1[0])
	#saves the file in the local with the image name
	# req.urlretrieve(imagesource, name)
	#clicks on the next image
	driver.find_element_by_xpath("//span[@title='Next image result']").click()
	time.sleep(3)

driver.close()






