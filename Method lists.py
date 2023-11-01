spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('hi'))

spam = ['hello', 'hi', 'howdy', 'heyas', 'hello']
print(spam.index('hello'))

spam2 = ['cat', 'dog', 'bat']
spam2.append('moose')
print(spam2)

spam3 = ['cat', 'dog', 'bat']
spam3.insert(1, 'chicken')
print(spam3)

spam4 = ['cat', 'dog', 'bat']
spam4.remove('dog')
print(spam4)

spam5 = [2, 5, 3.14, 1, -7]
spam5.sort()
print(spam5)

spam5 = [2, 5, 3.14, 1, -7]
spam5.sort(reverse=True)
print(spam5)

spam6 = ['Alice', 'bob', 'Carol', 'andrew', 'Zara']
spam6.sort()
print(spam6)

spam6 = ['Alice', 'bob', 'Carol', 'andrew', 'Zara']
spam6.sort(key=str.lower)
print(spam6)