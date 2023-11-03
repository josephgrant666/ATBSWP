#This is a program that checks whether a phone number is from the USA or Canada

def isPhoneNumber(text):
    if len(text) != 12:
        return False # Phone number not recognised 
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #No area code 
    if text[3] != '-':
        return False # Missing dash
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False # No first 3 digits 
    if text[7] != '-':
        return False # Missing second dash 
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # No last 4 digits
    return True 
    
print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber('415-5551234'))

message = 'Call me at 415-555-0000 tomorrow, or at 415-555-1234 today.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')

# This is a lot of code for a simple program. Therefore Coders have developed what are called 'Regular expressions' to help shorten this. 
# Here's the same program, but using regular expressions instead.

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobject = phoneNumRegex.search(message)
matchobject.group()
print(matchobject.group())
# This is a lot less code, but does only return the first instance it finds.
# Use the .findall method to return all results:

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))

# Part of an expression can be found in a list/string using the pipe character or |
# For example, if I wanted to find all instances of bat vehicle:

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())