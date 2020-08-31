import subprocess
import hachoir
import os
import json
from multiprocessing import Process, current_process

source = "D:\\Python-ds\\Images\\"
exe = "hachoir-metadata"

MetaData = {
    "data" : [
    ]
}
"""
gets the metadata of the file
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
    process_id = os.getpid()
    print(f"Process Id : {process_id}") # getting the process id printed
"""
Prints the metadata to json file
"""
def printjson():
    with open("jsonfile2.json", "w") as file:
        json.dump(MetaData, file)
    process_id = os.getpid()
    print(f"Process Id for json: {process_id}") # getting the process id printed


if __name__ == '__main__':
    processes = []
    for filename in os.listdir(source):
        process = Process(target = imageMetadata, args= (filename,)) # Giving the process route
        processes.append(process)
        process.start() # starts the processs
        process.join() # used to make the process execute one by one
        process1 = Process(target = printjson, args = ())
        processes.append(process1)
        process1.start()
    


