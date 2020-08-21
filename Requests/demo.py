from bs4 import BeautifulSoup
import urllib.request as req
import requests

r = requests.get("https://www.bing.com/images/search?scenario=ImageBasicHover&cw=1349&ch=695&q=animals&qft=+filterui:license-L2_L3_L4&form=IRFLTR&first=1")
content = r.content
soup = BeautifulSoup(content)
images = soup.find_all('img')
i = 1
for image in images:
	name = str(i) + ".jpg"
	imagename = image['src']
	req.urlretrieve(imagename, name)
	i += 1
