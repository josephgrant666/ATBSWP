import pyautogui
pyautogui.typewrite('', interval=0.2) # Sends key clicks to the computer with the interval given 
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.2) # This clicks the keyboard with the list of strings given 
pyautogui.KEYBOARD_KEYS # Lists the names of the keyboard keys 
pyautogui.press('f1') # Presses a key of your choice
pyautogui.hotkey('ctrl', 'o') # Presses hotkey shortcuts 