from bs4 import BeautifulSoup
import urllib.request as req
import requests
import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

parentDirectory = "D:\\Python-ds\\Python-ds\\Tkinter" #Parent directory
mainUrl = "https://e4ftl01.cr.usgs.gov/MOTA/MCD43A4.006/" # main url from which we get the data

r = requests.get(mainUrl)
content0 = r.content
soup = BeautifulSoup(content0, features = "lxml")
images = soup.find_all('a')
urls =[]
for image in images:
    href = str(image).split(">")
    urladd = href[1].split("<")
    urls.append(urladd[0])
urls = urls[7:]

def download(urlstart):
    updatestr = mainUrl + urlstart #updating the url to get into the date
    year, month, date = urlstart.split(".")
    yearpath = os.path.join(parentDirectory,year)
    if( not os.path.exists(yearpath)):
        os.mkdir(yearpath)
    monthpath = os.path.join(yearpath, month)
    if( not os.path.exists(monthpath)):
        os.mkdir(monthpath)
    datepath = os.path.join(monthpath, date)
    if (not  os.path.exists(datepath)):
        os.mkdir(datepath)
    abi = requests.get(updatestr)
    content1 = abi.content
    soup1 = BeautifulSoup(content1, features = "lxml")
    href = soup1.find_all('a')
    imageurl = []
    j = 0
    for h in href:
        i = str(h).split("\"")
        imageurl.append(i[1])
        imagelink = updatestr + i[1] # getting the image
        j += 1
        ext = ".jpg"
        if ext in imagelink:
            os.chdir(datepath)
            req.urlretrieve(imagelink, i[1])



# if __name__ == '__main__':
#     with ThreadPoolExecutor(max_workers = 12) as executor: # starts the Threadpool executor with 6 threads
#       results = executor.map(download, urls) # Maping the process to the threadpool


if __name__ == '__main__':
    pool = Pool() # Initializing the pool 
    pool.map(download, urls) # Starting the process pool
    pool.close()
    pool.join()
