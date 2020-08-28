"""
Trail 4
Using the hachoir package
Executes properly and gives the desired output but the execution time is
"""
import subprocess
import hachoir
import os
import json

source = "D:\\Python-ds\\Images\\"
exe = "hachoir-metadata"

MetaData = {
    "data" : [
    ]
}

def imageMetadata(filename):
    input_file = os.path.join(source, filename)
    process = subprocess.Popen([exe, input_file], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    for output in process.stdout:
        output = str(output)
        check = output.split("b'")
        data = check[1].split(":")
        dictionary = {
        data[0] : data[1]
        }
        MetaData["data"].append(dictionary)


for filename in os.listdir(source):
        imageMetadata(filename)


with open("jsonfile2.json", "w") as file:
    json.dump(MetaData, file)







"""
Trail 3
Using exif package
used to modify the data with the new metadata
"""
from exif import Image
with open('Image.jpg', 'rb') as image_file:
    my_image = Image(image_file)
if(my_image.has_exif):
    print(my_image.get_file())
"""
Trail 2
Got error with the keyword metadata
was unable to find the solution in internet.
"""


from importlib_metadata import version, metadata

with open("readme.txt", "r") as image:
    pass
print(metadata(image))

"""
Trail 1
Tried using the PILLOW package.
Execution time is a bit fast compared to the hachoir but metadata for some images is not loading.
Also for some images metadata has some binary data.
"""

from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open("Image.jpg")
exifdata = image.getexif()
# iterating over all EXIF data fields
imagedict = {
    "Imagename" : image.filename,
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
        data = data.decode()
    imagedict[tag] = data
# imagedict["metadata"].append(dictionary)
print(imagedict)
print("Next Image")