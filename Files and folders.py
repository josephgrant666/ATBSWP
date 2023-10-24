import os

os.path.join('folder1', 'folder2', 'folder3', 'file.png') # If you want to print a string that shows the file path on any operating system, then use the following function: 
os.sep()
os.getcwd()     # This finds the file path of a file. The current working directory is the folder that s being worked on at the moment 
os.chdir(path)  # This changes the CWD of a file
os.path.abspath(path) # This finds the absolute file path 
os.path.isabs(s) # This is a way of checking whether a file path begins with a relative path 
os.path.relpath(path) # This is a way of producing a relative file path 
os.path.dirname(p) # Retrieves the directory part of a file path 
os.path.basename(p) # Retrieves the last part of a file path 
os.path.exists(path) # Checks whether a file path exists 
os.path.isfile(path) # Checks  whether a path name is referring to a file 
os.path.isdir() # Checks  whether a path name is referring to a directory  
os.path.getsize(filename) # Returns the size of a file path in bytes as an integer
os.listdir() # Returns a string of a list of file names and list names of a file path


# Here's a program that retrieves the file sizes of all files in a folder
totalSize = 0 
for filename in os.listdir('N:\Documents\GTJ'):
    if not os.path.isfile(os.path.join('N:\Documents\GTJ')):
        continue
    totalSize = totalSize + ospath.getsize(os.path.join('N:\Documents\GTJ'))

os.makedirs(name) # Used to create new folders
