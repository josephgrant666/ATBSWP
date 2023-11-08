import re

# The ? character is used to refine a serach to zero or one times.
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 123-456-7890')
print(mo.group())

# This can be cancelled out by using \ For example:
dinnerRegex = re.compile(r'\w\w\w\w\w\w\\?')
mo = dinnerRegex.search('What do you want for dinner?')
print(mo.group())
# Returns 'Dinner' rather than 'Dinner?'

# The * character means zero or more times 
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowowowowowoman')
print(mo.group())

# The + character means one or more times 
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
# Here, 'Batwoman' is returned because it appears once or more. 'Batman' appears zero times, so it is not returned.

# If you wanted to match a specific number of iterations in a group, then use {}
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('I laughed out loud. HaHaHa')
print(mo.group())

# If you want to match a range of possible repetitions. Then {} can also be used:
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('I laughed out loud. HaHaHaHa')
print(mo.group())

# If you want to match a range of possible repetitions, but without the longest possible result, then ? can also be used:
haRegex = re.compile(r'(Ha){3,5}?')
mo = haRegex.search('I laughed out loud. HaHaHaHa')
print(mo.group())
