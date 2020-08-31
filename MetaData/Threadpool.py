import subprocess
import hachoir
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor
source = "D:\\Python-ds\\Images\\"
exe = "hachoir-metadata"
"""
Notes the Start time
"""
start_time = time.time()
"""
MetaData dictionary
"""
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
        if data[0] == "Metadata":
            data[1] = filename
        dictionary = {
        data[0] : data[1]
        }
        MetaData["data"].append(dictionary)
    printjson() # calls the printjson to write the data to json file

    
"""
Prints the metadata to json file
"""
def printjson():
    with open("jsonfile5.json", "a") as file:
        json.dump(MetaData, file)



if __name__ == '__main__':
    processes = []
    for filename in os.listdir(source):
        processes.append(filename)


    with ThreadPoolExecutor(max_workers = 6) as executor: # starts the Threadpool executor with 6 threads
      results = executor.map(imageMetadata, processes) # Maping the process to the threadpool
    print("--- %s seconds ---" %(time.time() - start_time)) # To get the execution time


