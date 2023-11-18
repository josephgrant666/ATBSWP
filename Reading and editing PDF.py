import os, PyPDF2 # Sometimes some PDF files will not be able to be opened using this module
pdfFile = open('meetingminutes1.pdf', 'rb') # Passed with 'rb' to read binary 
reader = PyPDF2.PdfFileReader(pdfFile) # This will return a new readable pdf object for this file 
reader.numPages # Returns how many pages there are 
reader.getPage(0) # This returns a page object, pages start at 0 
page.extractText() # Returns the text as one string 
# These functions are limited to changing pages or getting text from them, but text cannot be changed in the same way that it is for plaintext files

# Here's the code for a program that combines the pages of 2 PDF files 
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF1.PdfFileReader(pdf1File)
reader1 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter() # This is created to create a new object that combines the two files
for pageNum in range (reader1.numPages): # This for loop will add pages to the blank pdf object created before 
    page = reader1.getPage(pageNum) # This obtains the page object
    writer.addPage(page) # This loops through all of the pages in the pdf, gets the amount of pages and then adds them to the writer object 

for pageNum in range (reader2.numPages): # This for loop does exactly the same thing but now adds the pages from the 2nd pdf
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()