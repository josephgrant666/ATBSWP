import re 

song = '''On the first day of Christmas, my true love sent to me
A partridge in a pear tree
On the second day of Christmas, my true love sent to me
Two turtledoves
And a partridge in a pear tree
On the third day of Christmas, my true love sent to me
Three French hens
Two turtledoves
And a partridge in a pear tree
On the fourth day of Christmas, my true love sent to me
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the fifth day of Christmas, my true love sent to me
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the sixth day of Christmas, my true love sent to me
Six geese a-laying
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the seventh day of Christmas, my true love sent to me
Seven swans a-swimming
Six geese a-laying
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the eighth day of Christmas, my true love sent to me
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the ninth day of Christmas, my true love sent to me
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the tenth day of Christmas, my true love sent to me
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the eleventh day of Christmas, my true love sent to me
I sent eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
On the twelfth day of Christmas, my true love sent to me
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five gold rings (five golden rings)
Four calling birds
Three French hens
Two turtledoves
And a partridge in a pear tree
And a partridge in a pear tree '''

# We can use the findall function to return a list of string values. This does not create a match object
# This would be used to find all instances of the word 'Ten' 
songRegex = re.compile(r'Ten')
print(songRegex.findall(song))

# This would be used to find all 4 letter words
songRegex = re.compile(r'\s\w\w\w\w\s')
print(songRegex.findall(song))

# This would be used to find all vowels. Brackets are used to create your own character classes.
songRegex = re.compile(r'[aeiouAEIOU]')
print(songRegex.findall(song))

# This would be used to find all instances of 2 vowels in a row
songRegex = re.compile(r'[aeiouAEIOU]{2}')
print(songRegex.findall(song))

# This would be used to find all characters that are not vowels 
songRegex = re.compile(r'[^aeiouAEIOU]') # This is the same as doing [a|e|i|o|u|A|E|I|O|U]
print(songRegex.findall(song))

# This would be used to find all 'number' + object lyrics
songRegex = re.compile(r'\[One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve]\s\w+')
print(songRegex.findall(song))

