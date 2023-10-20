print('Hello, is it raining?')
answer1 = input()

if answer1 == 'yes':
    print('Do you have an umbrella?')
    answer2 = input()
    if answer2 == 'yes': 
        print('Go outside')
    if answer2 == 'no':
        print('Is it raining now?')
    answer3 = input()
    if answer3 == 'yes':
        print('wait a bit longer')

if answer1 == 'no':
    print('Go outside')
