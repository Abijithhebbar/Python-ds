import os
import json
from PIL import Image

"""
Gives the folder path
"""
directory = 'D:\\Python-ds\\Image scrapping'

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
	file = "D:\\Python-ds\\Image scrapping\\" + filename # getting the image
	img = Image.open(file) # Opens the Image with the Image method
	conf = 0.99
	"""
	Loops for 5 times to get the 5 duplicates
	"""
	for i in range(1,6):
		dup = img.copy() # Copies the images i.e., creates duplicates
		saveImg = name[0] + "_" + str(i) + ext # creating the filename for the duplicates
		dup.save(saveImg) # saves the image with the name
		conf += 0.001
		imageDict = { # adding the image values to the dictionary
		"file" : saveImg,
		"detections" : [
		{
		"conf": conf,
		"category" : i
		}
		],
		"max_detection_conf" : conf
		}
		outputDict["images"].append(imageDict) # appending the values to the Images key in the dictionary

"""
Loops through the given directory to iterate through all the files
"""
for filename in os.listdir(directory):
    if filename.endswith(".jpg"): # checks the files with .jpg extension
    	ext = ".jpg"
    	"""
    	Calls the imagesave method to get the duplicates
    	"""
    	imagesave(filename, ext)
    elif filename.endswith(".png"): # checks the files with .png extension
    	ext = ".png"
    	"""
    	Calls the imagsesave method to get the duplicates
    	"""
    	imagesave(filename, ext)
    elif filename.endswith(".jpeg"): # checks the files with .jpeg extension
    	ext = ".jpeg"
    	"""
    	Calls the imagesave method to get the duplicates
    	"""
    	imagesave(filename, ext)
    elif filename.endswith(".gif"): # checks the files with .gif extension
    	ext = ".gif"
    	"""
    	Calls the imagesave method to get the duplicates
    	"""
    	imagesave(filename, ext)


"""
Writes the Json to the local file
"""
with open("jsonfile.json", "w") as json_file:
	json.dump(outputDict, json_file)

