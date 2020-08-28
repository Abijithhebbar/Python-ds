Aim:
To create 5 Duplicate images for the single image and store the image details in a json file


Packages used : OS, JSON, shutil
OS used to Iterate through the local folder to get the files
JSON used to convert the dictionary to JSON
Shutil is used to copy the file


Method : imagesave
It is used to duplicate the images and save that locally.
It takes filename and extension as parameters.
It also appends the dictionary with the Required Image details


This programs checks for all the image files in the given folder and duplicates the images 5 times.
After the duplication is done all the details are added to the JSON and save that JSON locally.


New Files added:
Metadata.py : Got the metadata of the files with hachoir package.
TryMultiprocessing.py : Tried multiprocessing but was unable to get the desired result.
Demo.py : Added all the methods that I have tried to get the Metadata of the file
TryMultithreading.py : Tried the multithreading and it worked

