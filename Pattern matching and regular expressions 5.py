import re

# You can also use the carat symbol on regular expressions
beginswithHelloRegex = re.compile(r'^Hello')
print(beginswithHelloRegex.search('Hello there!'))

# The search below returns as none, because the search method only looks at the beginning of the string
print(beginswithHelloRegex.search('He said hello there!'))

# The dollar sign can be used to search the end of a string
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))

# Both the carat and dollar symbols can be used to check if an entire string is matched
entireStringRegex = re.compile(r'^Hello world!$')
print(entireStringRegex.search('Hello world!'))

# This can be used for pattern matching as well
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('12345678900987654321'))

# A full stop character can be used to mean any character beforehand
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat sat on the flat mat'))

# The star character can be used to find any pattern
atRegex = re.compile(r'(.*at)')
print(atRegex.findall('The cat sat on the flat mat'))

# The star character is greedy; it will look for all values. Add a question mark to make it non-greedy.
atRegex = re.compile(r'(.*?at)')
print(atRegex.findall('The cat sat on the flat mat'))

# The star function will not search new lines of code. Therefore the argument re.DOTALL has to be passed for this to search beyond a new line
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

# The re.ignore or re.i function can also be used to search text in a non-case sensitive way
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile(r'[aeiou]', re.I)
print(dotStar.findall(prime))