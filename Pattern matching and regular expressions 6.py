import re
# The sub() method can be used to regular text within a string 
# Here's an original piece of text 
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave secret documents to Agent Bob'))

# Here's the same text, but with the sub method being used 
print(namesRegex.sub('REDACTED', 'Agent Alice gave secret documents to Agent Bob'))

# Say however that we wanted to substitute a part of a phrase. Here we can use the \1 and \2 and so on method 
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1*****', 'Agent Alice gave secret documents to Agent Bob'))

# Verbose regular expressions can be used to make more sense of long regular expressions. For example:
re.compile(r'\(d\d\d)(-)?\d\d\d-\d\d\d\d')
# Can be turned into:
re.compile(r'''\(d\d\d-|  # Area code (without brackets and with dash)
(\(\d\d\d\))              # Area code (with brackets and no dash)
-                         # First dash
\d\d\d                    # First 3 digits 
-                         # Second dash 
\d\d\d\d                  # Last 4 digits 
\sx\d{2,4},               # extension, like x1234''', re.VERBOSE | re.I | re.DOTALL)
# Which is a lot more readable than before. The # comments are technicially a part of the pattern matching code, but are not executed in any way. 
# Multiple functions can also be passed using the | character (look at line 23)

