import mysql.connector
from bs4 import BeautifulSoup
import urllib.request as req
import requests


parentDirectory = "D:\\Python-ds\\Python-ds\\Tkinter\\Check" #Parent directory
mainUrl = "https://e4ftl01.cr.usgs.gov/MOTA/MCD43A4.006/" # main url from which we get the data
print("Please enter the date")

date = input()
date = date.replace("-", ".")
date = date + "/"
r = requests.get(mainUrl)
content0 = r.content
soup = BeautifulSoup(content0, features = "lxml")
images = soup.find_all('a')
urls =[]
for image in images:
    href = str(image).split(">")
    urladd = href[1].split("<")
    urls.append(urladd[0])
start = urls.index(date)
urls = urls[start:]
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abijith123",
  database="mydatabase"
)
mycursor = mydb.cursor()
for urlstart in urls:
	urlstart = str(urlstart).replace(".", "-")
	sql = """INSERT INTO checktable (dateof) VALUES  (%s)"""
	mycursor.execute(sql, urlstart)
	print(urlstart)
	mydb.commit()

