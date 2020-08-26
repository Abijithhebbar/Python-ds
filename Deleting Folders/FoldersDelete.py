import os
import time
import shutil
"""
Path for the folder
"""
directory = 'D:\\'


"""
Getting the present time
"""
now = time.time()
"""
Storing exact 24 hours late in old varaible
"""
old = now - 24 * 60 * 60
"""
Loops through the folder and checks for the subfolders
"""
for filename in os.listdir(directory):
	Main_folder_path = os.path.join(directory, filename) # Joining the foldername to the path
	stat_result = os.stat(Main_folder_path) # getting the stats of the folder


	if stat_result.st_ctime < old: # checking the time of the creation of the folder if it is not created today
		try:
			shutil.rmtree(Main_folder_path) # Removes the folders which are older than a day.
		except:
			continue
