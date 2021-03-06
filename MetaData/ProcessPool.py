import subprocess
import hachoir
import os
import json
import time
from multiprocessing import Pool, current_process
source = "D:\\Python-ds\\Images\\"
exe = "hachoir-metadata"
"""
Noting the start time to get the execution time
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
    with open("jsonfile4.json", "a") as file:
        json.dump(MetaData, file)


if __name__ == '__main__':
    processes = []
    for filename in os.listdir(source):
        processes.append(filename)
    pool = Pool() # Initializing the pool 
    pool.map(imageMetadata, processes) # Starting the process pool
    pool.close()
    pool.join()
    print("--- %s seconds ---" %(time.time() - start_time)) # Displays the execution time
    


