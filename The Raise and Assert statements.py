import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol needs to be a length of 1.') # This exception is put in to anticipate any potential errors in the code that you think may occur. 
    if (width < 2) or (height < 2):
        raise Exception('The box needs to have a width and height of at least 2.')
              
    print(symbol * width)

    for i in range(height - 2 ):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

print(boxPrint('*', 10, 5))
print(boxPrint('O', 5, 15))

# The assert function means that: 'I assert that this condition is always true, and if not, then there is an error somewhere!' 

# Say we wanted to create program that runs a set of traffic lights:

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(switchLights(market_2nd))
# This assertion passes because after our code has passed, neither light is red, and so the assert statement becomes false and fires.



