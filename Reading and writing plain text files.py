helloFile = open(r'C:\Users\User\Documents\Python Projects\Hello world.txt') # Opens the file according to the path given
content = print(helloFile.read()) # Displays the plain text contents of that file as a list of strings
helloFile.close() # Closes the file that has been opened 
# helloFile.readlines() # Same as read but returns a single string
# helloFile.open(r'C:\Users\User\Documents\Python Projects\Hello world.txt', 'w') # This is the write mode, which allows changes to the plain text to be made. Changes overwrite the file entirely.
# helloFile.open(r'C:\Users\User\Documents\Python Projects\Hello world.txt', 'a') # This is the append mode, which allows changes to the plain text to be made. This changes a part of the file without overwriting. 
# If the file doesn't exist, python will create a new text file for you.

helloFile2 = open(r'C:\Users\User\Documents\Python Projects\Hello world 2.txt', 'w')
helloFile2.write('Hello!!!!!!\n' * 3) 
helloFile2.close
helloFile2 = open(r'C:\Users\User\Documents\Python Projects\Hello world 2.txt', 'a')
helloFile2.write('\n\nApples are tasty.')
helloFile2.close
# This is a good way for writing and reading a single, long string 

# However, if you want to read and write list that contain complex data structures like lists and dictionairies etc. Then you can save variables in your python program to binary shelf files in the shelve module.
import shelve
shelfFile = shelve.open('mydata') # This will return a shelf file object. You can make changes to this file as if it were a dictionary.
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close

shelfFile = shelve.open('mydata')
shelfFile['cats'] # I can call this to retrieve the dictionary values that have been stored
# The benefit of doing this is that you can save complex data structures and reopen them in python later on. 
shelfFile.close()

import os

print(os.getcwd())

# The shelve files are stored as three binary files. '.bak', '.dir' and '.dat'

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))