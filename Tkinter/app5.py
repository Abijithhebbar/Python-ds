from bs4 import BeautifulSoup
import urllib.request as req
import requests
import os
from concurrent.futures import ThreadPoolExecutor
import glob
import sqlite3




mycursor = sqlite3.connect('test.db') # Connecting sqlite db

parentDirectory = "D:\\Python-ds\\Python-ds\\Tkinter\\Check" #Parent directory
mainUrl = "https://e4ftl01.cr.usgs.gov/MOTA/MCD43A4.006/" # main url from which we get the data
print("Please enter date")
date = input()
date = date.replace("-", ".")
date = date + "/"
dic = {}
r = requests.get(mainUrl) # getting the url page
content0 = r.content
soup = BeautifulSoup(content0, features = "lxml")
images = soup.find_all('a') # finding the hyperlinks and targetting that


sql = "SELECT id FROM data" # gets the id's of the exisisting or alreacy downloaded data
dataInDb = mycursor.execute(sql)
myresult = dataInDb.fetchall() 
checklist = []
#this loop is to preprocess the data received from the db
for i in myresult:
    checklist.append(list(i))
checklist2= []
for sublist in checklist:
    for val in sublist:
        checklist2.append(val)




urls =[]
# with this loop we get the image urls
for image in images:
    href = str(image).split(">")
    urladd = href[1].split("<")
    urls.append(urladd[0])
start = urls.index(date)
urls = urls[start:]
# with this loop we remove the dates which are alreacy downloaded
for ele in checklist2:
    if ele in urls:
        urls.remove(ele)
"""
Input given is the date
downloads all the image files of the given date
and also stores the required info in dictionary
"""
def download(urlstart):
    print(urlstart)
    updatestr = mainUrl + urlstart #updating the url to get into the date
    year, month, day = urlstart.split(".") # splitting the date to create year , month, date folder

    yearpath = os.path.join(parentDirectory,year)
    if( not os.path.exists(yearpath)):
        os.mkdir(yearpath) # setting the directory
    monthpath = os.path.join(yearpath, month)
    if( not os.path.exists(monthpath)):
        os.mkdir(monthpath) # setting the month directory
    datepath = os.path.join(monthpath, day)
    if (not  os.path.exists(datepath)):
        os.mkdir(datepath) #setting the date directory
    abi = requests.get(updatestr)
    content1 = abi.content
    soup1 = BeautifulSoup(content1, features = "lxml")
    href = soup1.find_all('a') # getting all  the hyperlinks
    j = 0
    for h in href:
        i = str(h).split("\"") #getting the image name
        imagelink = updatestr + i[1] # getting the image
        ext = ".jpg" # catching only image files
        if ext in imagelink:
            os.chdir(datepath) # setting the dwonload path
            req.urlretrieve(imagelink, i[1])
    countofimages = str(datepath)
    countImages = countofimages.replace("\\", "/") # preprocessig the path to count the number of images
    countImages = countImages + "/*"
    count = os.path.normpath(countImages)
    ImagesCount = glob.glob(count) # counting the images
    # adding the values to dictionary
    if urlstart not in dic:
        dic[urlstart] = []
        dic[urlstart].append(urlstart)
        dic[urlstart].append(str(updatestr))
        dic[urlstart].append(len(ImagesCount))
    else:
        dic[urlstart].append(len(ImagesCount))



if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers = 4) as executor: # starts the Threadpool executor with 6 threads
      results = executor.map(download, urls) # Maping the process to the threadpool
    print(dic.values())
    #updating the db
    sql=" INSERT INTO data (id, imageurl, images)\
    VALUES (?, ?, ?)"
    mycursor.executemany(sql, dic.values())
    mycursor.commit()


