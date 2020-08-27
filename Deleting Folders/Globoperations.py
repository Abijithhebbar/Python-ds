import glob
import os
import time
import shutil
# """
# Path for the folder
# """
# directory = 'D:\\check folder - Copy'


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

# subfolders = [os.path.join(directory, folder) for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory,folder))]
subfolders = glob.glob('D:\\dummy\\*\\')
for i in subfolders:
	stat_result = os.stat(i)
	if stat_result.st_mtime < old:
		shutil.rmtree(i)