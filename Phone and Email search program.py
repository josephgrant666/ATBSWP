#! python3

import re
import pyperclip

# Create regex for phone numbers
phoneRegex = re.compile(r''' 
# Possible formats: 415-123-0000, 123-0000, (415) 123-0000, 123-0000 ext. 12345, ext. 12345, x12345
(                           # Added so that everyting is searched as one group
(\d\d\d | (\(\d\d\d\)))?    # Area code (optional)
(\s|-)                      # First seperator
\d\d\d                      # First 3 digits 
-                           # Second seperator 
\d\d\d\d                    # Last 4 digits 
((ext(\.)?\s |x)            # Extension word part (optional)
(\d{2,5}))?                 # Extension number part (optional)
)                           # Added so that everyting is searched as one group
''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r''' 
# Possible formats: some.+_thing@(\d{2,5}))).com

[a-zA-z0-9_.]+  # Name part 
@               # @ symbol
[a-zA-z0-9_.]+  # Domain name part 
''', re.VERBOSE)

# TODO: Get text off the clipboard 
text = pyperclip.paste()

# TODO: Extract email/phone numbers from the text 
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted email/phone to the clipboard
'\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

