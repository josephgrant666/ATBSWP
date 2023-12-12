print(list('Joseph Grant'))

name = 'Joseph Grant'
print(name[0])
print(name[3:5])
print(name[-2])
print('Jo' in name)
print('xxx' in name)
for letter in name:
    print(letter)

name2 = 'Joe a cat'
newName = name2[0:3] + ' the ' + name2[6:9]
print(newName)

# Variables don't contains lists, they contain a reference to the list 
spam = [0, 1, 2, 3, 4, 5]
cheese = spam 
cheese[1] = 'hello!'
print(cheese)
print(spam)

def eggs(cheese):
    cheese.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)

spam = ['apples',
        'oranges',
        'bananas',
        'cats']
print('Four score and seven ' + \
      'years ago')