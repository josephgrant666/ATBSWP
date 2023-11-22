import pyautogui
pyautogui.screenshot('FILEPATH') # Returns a Pillow image object and saves it to the given filepath
pyautogui.locateOnScreen('FILEPATH OF SCREEN IMAGE YOU NEED') # Returns the coordinates of the thing you want to find on the screen, and its width and height
pyautogui.locateCenterOnScreen('FILEPATH OF SCREEN IMAGE YOU NEED') # Returns the coordinates of the thing you want to find on the screen right in the centre of the image
