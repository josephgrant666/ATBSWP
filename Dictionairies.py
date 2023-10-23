myCat = {'size': 'fat', 'colour': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['colour'] + ' fur')

spam = {12345: 'Luggage combination', 42: 'The answer'}
eggs = {42: 'The answer', 12345: 'Luggage combination'}
print(spam == eggs)

print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()))

for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

for i in myCat.items():
    print(i)

for k, v in myCat.items():
    print(k, v)

print(myCat.get('size', 0))
print(myCat.get('color', ''))

print('My cat is ' + str(myCat.get('size', ' not fat' )) + ' and I love him')
print('My cat is ' + str(myCat.get('fat', 'not fat' )) + ' and I love him')

if 'hefty' not in myCat:
    myCat['hefty'] = 'chonky'
    print(myCat)
print(myCat.setdefault('hefty', 'not too bad'))