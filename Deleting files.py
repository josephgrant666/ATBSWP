import os 

os.unlink(r'C:\Users\User\Documents\DELETE_THIS.jpg') # A function that can be used to delete a file 

os.rmdir(r'C:\Users\User\Documents\Custom Office Templates') # An entire folder can be removed using this remove directory function
# To call this, the folder has to be completely empty 

import shutil
# If you do want to remove a folder and all of its contents, then the shutil module has to be imported, and this function is called:
shutil.rmtree(r'C:\Users\User\Documents\Screencast-O-Matic')

# THESE FUNCTIONS WILL PERMENANTLY REMOVE FOLDERS AND FILES - THEY ARE NOT SENT TO THE RECYCLING BIN!

# This can be safeguarded against by using the 'Dry run' method; which is where any of these functions are #'ed out first, and the filename is printed before you then decide to delete it

import send2trash # However, the send2trash module avoids any permanent deletion.
send2trash.send2trash('Filename') # Executes this code 