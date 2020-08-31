Files:
ThreadPool.py - Used the threadpool to get the metadata
Processpool.py - Used the Processpool to get the metadata
metaData.py - Gets the metadata with the help of hachoir
Trymultithreading.py - Tried the multithreading to get the metadata.
TrymultiProcessing.py - Tried the multiprocessing to get the metadata
metadata2.py - Gets the metaData with the help of the PILLOW package
demo.py - Displayed all the type of methods tried to get the metadata.


Packages used:
Subprocess - to get the subprocess of the process
hachoir - to get the metadata of the files
os - to access the local files
json - to jsonify the dictionary data
time - to get the start time and determine the package run time.
concurrent.futures -  to use the threadpool feature
multiprocessing - to use the processpool and the current_process methods.



Methods used:
imageMetadata - this method gets the filename and returns the metadata in the form of a dictionary.
Later the dictionary is converted to a json and written locally and stored.