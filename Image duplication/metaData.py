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

