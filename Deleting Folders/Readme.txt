Aim:
To delete all the sub folders in a given folder that is not created today.

Packages used:
OS to direct to the path of the folders
TIME to get the present time
Shutil to perform the delete operation of the folder
GLOB to route through the give folder to find the specific files or folders

In the for loop it iterates through all the sub folder in the given path.
then checks the date of creation and deletes all the subfolders which are created more than 24 hrs ago.
