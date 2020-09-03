from bs4 import BeautifulSoup
import urllib.request as req
import requests
import os

year = "2020"
month = "04"
date = "28"
mainUrl = "D:\\Python-ds\\Python-ds\\Tkinter"
yearpath = os.path.join(mainUrl,year)
os.mkdir(yearpath)
monthpath = os.path.join(yearpath, month)
os.mkdir(monthpath)
datepath = os.path.join(monthpath, date)
os.mkdir(datepath)

r = requests.get("https://www.iiit.ac.in/")
content0 = r.content
soup = BeautifulSoup(content0)
images = soup.find_all('img')
i = 1
for image in images:
	os.chdir(datepath)
	name = str(i) + ".jpg"
	imagename = image['src']
	req.urlretrieve(imagename, name)
	i += 1


