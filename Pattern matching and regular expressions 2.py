import re 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My Number is 415-555-1234')
print(mo.group())
# This code returns the entire number, but what if we wanted a part of it?
# We can use the group method to mark out parts of the pattern by using perenthesis:

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My Number is 415-555-1234')
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))