import pprint

message = 'It was a bright day in April and the clocks were striking thriteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1 

print(count)

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1 

pprint.pprint(count)