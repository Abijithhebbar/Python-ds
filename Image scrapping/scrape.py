import time
from selenium import webdriver
import urllib.request as req
import requests


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
# list for Image names
imagename = ["1.jpg", "2.jpg", "3.jpg", "4.jpg" , "5.jpg", "6.jpg" , "7.jpg" , "8.jpg" , "9.jpg", "10.jpg",
"11.jpg", "12.jpg", "13.jpg", "14.jpg" , "15.jpg", "16.jpg" , "17.jpg" , "18.jpg" , "19.jpg", "20.jpg",
"21.jpg", "22.jpg", "23.jpg", "24.jpg" , "25.jpg", "26.jpg" , "27.jpg" , "28.jpg" , "29.jpg", "30.jpg",
"31.jpg", "32.jpg", "33.jpg", "34.jpg" , "35.jpg", "36.jpg" , "37.jpg" , "38.jpg" , "39.jpg", "40.jpg",
"41.jpg", "42.jpg", "43.jpg", "44.jpg" , "45.jpg", "46.jpg" , "47.jpg" , "48.jpg" , "49.jpg", "50.jpg",
"51.jpg", "52.jpg", "53.jpg", "54.jpg" , "55.jpg", "56.jpg" , "57.jpg" , "58.jpg" , "59.jpg", "60.jpg",
"61.jpg", "62.jpg", "63.jpg", "64.jpg" , "65.jpg", "66.jpg" , "67.jpg" , "68.jpg" , "69.jpg", "70.jpg",
"71.jpg", "72.jpg", "73.jpg", "74.jpg" , "75.jpg", "76.jpg" , "77.jpg" , "78.jpg" , "79.jpg", "80.jpg",
"81.jpg", "82.jpg", "83.jpg", "84.jpg" , "85.jpg", "86.jpg" , "87.jpg" , "88.jpg" , "89.jpg", "90.jpg",
"91.jpg", "92.jpg", "93.jpg", "94.jpg" , "95.jpg", "96.jpg" , "97.jpg" , "98.jpg" , "99.jpg", "100.jpg"]
# Catches the image page
driver.get(ImageUrl)
time.sleep(3)
for i in range(0,100):
	# imagesource = driver.find_element_by_tag_name("img").get_attribute("src")
	#selects the src of the image i.e., url
	imagesource= driver.find_element_by_xpath("//*[@id='mainImageWindow']/div[1]/div/div/div/img").get_attribute("src")
	time.sleep(4)
	print(imagesource)
	#saves the file in the local with the given name
	req.urlretrieve(imagesource, imagename[i])
	time.sleep(5)
	#clicks on the next image
	driver.find_element_by_xpath("//span[@title='Next image result']").click()
	time.sleep(3)

driver.close()






