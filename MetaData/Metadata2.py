from PIL import Image
from PIL.ExifTags import TAGS
import os
from threading import Thread
import json

source = "D:\\Python-ds\\Images\\"

MetaData = {
    "Image" : [
    ]
}



def ImageMetaData(filename):
    file = os.path.join(source, filename)
    image = Image.open(file)
    exifdata = image.getexif()
    # iterating over all EXIF data fields
    imagedict = {
    }
    print(image.filename)
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        # print(tag)

        data = exifdata.get(tag_id)
        # print(f"Data : {data}")
        # decode bytes 
        if isinstance(data, bytes):
            data = str(data)
        imagedict[tag] = data
    MetaData["Image"].append(imagedict)


for filename in os.listdir(source):
    ImageMetaData(filename)

with open("jsonfile3.json", "w") as jsonfile:
    json.dump(MetaData, jsonfile)






























# image = Image.open("Image.jpg")
# exifdata = image.getexif()
# # iterating over all EXIF data fields
# imagedict = {
#     "Imagename" : image.filename,
#     "metadata" : [
#     ]
# }
# print(image.filename)
# dictionary = {}
# for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag = TAGS.get(tag_id, tag_id)
#     # print(tag)

#     data = exifdata.get(tag_id)
#     # print(f"Data : {data}")
#     # decode bytes 
#     if isinstance(data, bytes):
#         data = data.decode()
#     dictionary[tag] = data
# imagedict["metadata"].append(dictionary)
# print(imagedict)
# print("Next Image")