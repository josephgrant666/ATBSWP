print('Are you playing?')
answer = input()
if answer == 'YES':
    print('Playing again')
if answer.lower() == 'yes':
    print('Playing again')

spam = 'Helloworld12345'
print(spam.islower())
print(spam.isupper())
print(spam.isalpha()) # to not create error message, the string must be blank
print(spam.isalnum())
print(spam.isdecimal())
print(spam.isspace()) # true if all parts being evauluated are a space/blank 
print(spam.istitle()) # true if all words start with upper case

print(spam.startswith('Hello'))
print(spam.endswith('Hello'))

print(','.join(['cats', 'rats', 'bats']))
print('My name is Joe'.split())
print('My name is Joe'.split('e'))

print('Hello'.rjust(10) + ' My name is Joe.')
print('Hello'.rjust(10, '*') + ' My name is Joe.')
print('Hello'.ljust(10) + 'My name is Joe.')
print('Hello'.ljust(10, '.') + 'My name is Joe.')
print('Hello'.center(10) + 'My name is Joe.')
print('Hello'.center(10, '.') + 'My name is Joe.')
print('        Hello         '.strip())
print('        Hello         '.lstrip())
print('        Hello         '.rstrip())
print('My name is Joe'.strip('e')) # takes away the first instance
print('My name is Joe'.replace('e', 'J'))

pyperclip.copy('Hi there')
print(pyperclip.paste())