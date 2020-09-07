from bs4 import BeautifulSoup
import urllib.request as req
import requests
import os
from concurrent.futures import ThreadPoolExecutor
import glob

parentDirectory = "D:\\Python-ds\\Python-ds\\Tkinter\\Check" #Parent directory
mainUrl = "https://e4ftl01.cr.usgs.gov/MOTA/MCD43A4.006/" # main url from which we get the data
print("Please enter the date")

date = input()
date = date.replace("-", ".")
date = date + "/"
dic = {}
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


def download(urlstart):
    updatestr = mainUrl + urlstart #updating the url to get into the date
    year, month, day = urlstart.split(".")

    yearpath = os.path.join(parentDirectory,year)
    if( not os.path.exists(yearpath)):
        os.mkdir(yearpath)
    monthpath = os.path.join(yearpath, month)
    if( not os.path.exists(monthpath)):
        os.mkdir(monthpath)
    datepath = os.path.join(monthpath, day)
    if (not  os.path.exists(datepath)):
        os.mkdir(datepath)
    abi = requests.get(updatestr)
    content1 = abi.content
    soup1 = BeautifulSoup(content1, features = "lxml")
    href = soup1.find_all('a')
    j = 0
    for h in href:
        i = str(h).split("\"") #getting the image name
        imagelink = updatestr + i[1] # getting the image
        ext = ".jpg"
        if ext in imagelink:
            os.chdir(datepath)
            req.urlretrieve(imagelink, i[1])
    countofimages = str(datepath)
    countImages = countofimages.replace("\\", "/")
    countImages = countImages + "/*"
    count = os.path.normpath(countImages)
    ImagesCount = glob.glob(count)
    print(len(ImagesCount))
    print(str(updatestr))
    if urlstart not in dic:
        dic[urlstart] = []
        dic[urlstart].append(urlstart)
        dic[urlstart].append(str(updatestr))
        dic[urlstart].append(len(ImagesCount))
    else:
        dic[urlstart].append(len(ImagesCount))



if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers = 12) as executor: # starts the Threadpool executor with 6 threads
      results = executor.map(download, urls) # Maping the process to the threadpool
    print(dic)

