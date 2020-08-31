import subprocess
import hachoir
import os
import json
import time
from threading import Thread
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
class thread1(Thread):
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

"""
writing to the json file
"""
class thread2(Thread):
    with open("Multithread.json", "w") as file:
        json.dump(MetaData, file)


thread1 = thread1()
thread2 = thread2()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("--- %s seconds ---" %(time.time() - start_time))
