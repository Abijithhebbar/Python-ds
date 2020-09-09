import os
import glob
from concurrent.futures import ThreadPoolExecutor
import sqlite3
from datetime import datetime, time, timedelta
import requests
import urllib.request as req
from bs4 import BeautifulSoup



mycursor = sqlite3.connect('database.db')
downloadData = {}
downloadPath = "D:\\Python-ds\\Python-ds\\downloads"
def main():
    """
    Main method gets the date and the url from the user.
    and sends that to scrapepage
    """
    print("enter the date")
    dateinp = input()
    print("Enter the web address")
    global url 
    url = input()
    if(requests.get(url)):
        print("it is a url")
        scrapePage(dateinp, url)
    else:
        print("you have not entered url")



def scrapePage(dateinp, url):
    """
    scrapePage gets the input from main method.
    scrapes through the given url.
    And gets all the dates from the page.
    if date is not present in the url page, it prints data not present
    If the date is present it calls the getdbdates method.
    where we get the dates on which the images are downloaded.
    then calls the threadlist method and sends the filtered dates for which images are not downloaded.
    """
    dateinp = dateinp.replace("-", ".")
    dateinp = dateinp + "/"
    r = requests.get(url)
    pageContent = r.content
    soup = BeautifulSoup(pageContent, features = 'lxml')
    dates = soup.find_all('a')
    getdates = []
    for date in dates:
        href = str(date).split(">")
        dateUrl = href[1].split("<")
        getdates.append(dateUrl[0])
    if dateinp not in getdates:
        datenotpresent = dateinp.replace(".","-")
        datenotpresent = datenotpresent[:-1]
        enddate = datetime.strptime(datenotpresent,'%Y-%m-%d')
        topdate = getdates[-1]
        datestart = topdate.replace(".", "-")
        datestart = datestart[:-1]
        startdate1 = datetime.strptime(datestart,'%Y-%m-%d')

        delta = enddate - startdate1
        for i in range(delta.days + 1):
            notpresentday = startdate1 + timedelta(days = i)
            print(f"Data not available for : {notpresentday}")


    else:
        startdate = getdates.index(dateinp)
        getdates = getdates[startdate:]
        # if the data is to be downloaded.
        # datenotdownloaded = dateinp.replace(".", "-")
        # datenotdownloaded = datenotdownloaded[:-1]
        # dateformatofnotdwonloaded = datetime.strptime(datenotdownloaded,'%Y-%m-%d')
        # sql = "SELECT id from data order by date(id) desc"
        # databasedate = mycursor.execute(sql)
        # getdbdates = databasedate.fetchall()
        # toplist =[]
        # for sublist in li:
        #     for val in sublist:

        #         dates = datetime.strptime(val, '%Y-%m-%d')
        #         toplist.append(dates)
        # delta = dateformatofnotdwonloaded - toplist[0]
        # updatedlist = []
        # if dateformatofnotdwonloaded > toplist[0]:
        #   delta = dateformatofnotdwonloaded - toplist[0]
        #   for i in range(delta.days + 1):
        #       addeddays = li1[0] + timedelta(days=i)
        #       addeddays = str(addeddays)
        #       addeddays = addeddays[0:10]
        #       addeddays = addeddays.replace("-", ".")
        #       addeddays = addeddays + "/"
        #       updatedlist.append(addeddays)
        # getdates = getdates + updatedlist
        finaldatelist = getdbDates(getdates)
        threads(finaldatelist)

def getdbDates(getdates):
    """
    gets the list of dates from scrapepage.
    and it returns the list of dates for which the images are not downloaded.
    """
    sql = "SELECT id from data"
    dbdata = mycursor.execute(sql)
    result = dbdata.fetchall()
    mainlist = []
    for sublist in result:
        for val in sublist:
            val = val.replace("-", ".")
            val = val + "/"
            mainlist.append(val)
    for element in mainlist:
        if element in getdates:
            getdates.remove(element)
    return getdates

def downloadImages(day):
    """
    gets the date for whic images are to be downloaded.
    downloads the images and stores the data in a dictionary.
    """
    dayurl = url + day
    year, month, date1 = day.split(".")
    yearpath = os.path.join(downloadPath,year)
    if( not os.path.exists(yearpath)):
        os.mkdir(yearpath)
    monthpath = os.path.join(yearpath, month)
    if( not os.path.exists(monthpath)):
        os.mkdir(monthpath)
    datepath = os.path.join(monthpath, date1)
    if (not  os.path.exists(datepath)):
        os.mkdir(datepath)
    datescrape = requests.get(dayurl)
    daycontent = datescrape.content
    datesoup = BeautifulSoup(daycontent, features = "lxml")
    images = datesoup.find_all('a')
    for image in images:
        i = str(image).split("\"")
        imagelink = dayurl + i[1]
        ext = ".jpg"
        if ext in imagelink:
            os.chdir(datepath)
            req.urlretrieve(imagelink, i[1])
    countofimages = str(datepath)
    countImages = countofimages.replace("\\", "/") # preprocessig the path to count the number of images
    countImages = countImages + "/*"
    count = os.path.normpath(countImages)
    ImagesCount = glob.glob(count)
    print(len(ImagesCount))
    if day not in downloadData:
        downloadData[day] = []
        day1 = day.replace(".", "-")
        day1 = day1[:-1]
        downloadData[day].append(day1)
        downloadData[day].append(dayurl)
        downloadData[day].append(len(ImagesCount))
    print(downloadData)






def threads(finaldatelist):
    """
    Called by scrapePage method it gives all the dates for which images are to be downloaded.
    it uses threadpoolexecutor to call the download method to download the images.
    then stores the data to db
    """
    with ThreadPoolExecutor(max_workers = 6) as executor:
        results = executor.map(downloadImages, finaldatelist)
    sql = "INSERT INTO data (id, imageurl, images)\
    VALUES (?, ?, ?)"
    mycursor.executemany(sql, downloadData.values())
    mycursor.commit()

if __name__ == '__main__':
    main()