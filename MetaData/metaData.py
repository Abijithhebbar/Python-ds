import subprocess
import hachoir
import os
import json
import time
"""
startTime
"""
start_time = time.time()
"""
Source path
"""
source = "D:\\Python-ds\\Images\\"
"""
hachoir command to get the metadata
"""
exe = "hachoir-metadata"
"""
Metadata dictionary
"""
MetaData = {
    "data" : [
    ]
}
"""
Recieves the filename from the folder
returns the metadata to the dictionaary
"""
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

"""
Looping through the source folder
"""
for filename in os.listdir(source):
        imageMetadata(filename)

"""
writing to the json file
"""
with open("jsonfile2.json", "w") as file:
    json.dump(MetaData, file)

print("--- %s seconds ---" %(time.time() - start_time)) # To display the execution time of the program.

