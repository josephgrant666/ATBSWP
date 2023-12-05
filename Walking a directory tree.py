import os

for folderName, subFolders, fileNames in os.walk(r'C:\Users\User\Documents\My Games'): # This function is used to make changes to files and folders in a path of folders
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The filenames in ' + folderName + ' are: ' + str(fileNames))
    print()
# The return value here uses a for loop and returns three values on each iteration
# The iterations are given by the variable names that I've given in the argument above 

# From here, code could be written to then manage the content of these folders