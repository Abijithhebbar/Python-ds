import os
import json
import shutil
from tqdm import tqdm
"""
Gives the folder path
"""
source = 'D:\\Python-ds\\Image scrapping'
"""
Giives the destination path
"""
destination = 'D:\\Python-ds\\Image duplication\\Pictures'

"""
Creates the dictionary
"""

outputDict = {
"info": {
 "time": "2020-07-30 06:04:53",
 "format_version": "1.0"
},
"detection_categories": {
 "2": "person",
 "3": "vehicle",
 "1": "animal"
},
"images": [
  ]
}

"""
This method creates the 5 duplicate images of the given file
@param input = filename and extension
output = Duplicates the image and saves it
"""
def imagesave(filename, ext):
    name = filename.split(ext) # used to split the file name with the extensions
    file = os.path.join(source, filename)
    conf = 0.99
    for i in range(1,6):
        saveImg = name[0] + "_" + str(i) + ext
        imageCopy = os.path.join(destination, saveImg)
        shutil.copy2(file, imageCopy)
        conf += 0.001
        imageDict = {
        "file" : saveImg,
        "detections" : [
        {
        "conf" : conf,
        "category" : i
        }
        ],
        "max_detection_conf" : conf
        }
        outputDict["images"].append(imageDict)



"""
Loops through the given directory to iterate through all the files
"""
for filename in tqdm(os.listdir(source)):
    extension = (".jpg", ".jpeg", ".png", ".gif") # creating a tuple with the valid extensions
    if filename.endswith(extension):
        getExtension = filename.split(".")
        ext = getExtension[-1]
        ext = "." + ext
        """
        Calls the imagesave method to get the duplicates
        """
        imagesave(filename, ext)


"""
Writes the Json to the local file
"""
with open("jsonfile.json", "w") as json_file:
    json.dump(outputDict, json_file)