name = 'Joe '
place = 'Main Street '
time = '18:00'
food = 'Party rings'
print('Hello ' + name + 'you are invited to a party at ' + place + 'at ' + time + '. Please bring ' + food + '.')
# this can be too long and compicated. So instead use this. These are called conversion specifiers:

print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, time, place, food))
