# Engineering_4_Notebook

## Python x Raspberry Pi

### Dice Roller

#### Assignment:
Create a Python program to run on your Pi that allows the user to roll/reroll a die by pressing ENTER and quit by pressing X and ENTER.

#### Code:
```python
# Automatic Dice Roller
# Written by Philip

import random
import pyautogui 
import time
import keyboard
min=1 #used for testing
max=6
active= True #my variables for my while loops to control when they are active
confirmState= False
print ("Automatic Dice Roller") #my intial setups to give instructions
print ("Press ENTER to roll")
print("Press X to Quit")
while active==True:
    if keyboard.is_pressed('enter'): #I'm using pyautogui which is a cool little tool I found that is helpful
        print(random.randint(min, max))
        time.sleep(.2) #makes it so that when you press it it does not spam
    if keyboard.is_pressed('x'): #quit logic
        print("Press ENTER to Confirm Quit")
        confirmState=True #enabled my confirm while loop
        time.sleep(.2) #again so it doesn't spam
        while confirmState ==True:
            if keyboard.is_pressed('enter'): 
                active=False #disabled my main loop
                time.sleep(.2) #anti spam again

                print("Quit")
                confirmState=False #disabled program completely 
```
#### What to Remember:
* Use pyautogui to detect key presses, https://pyautogui.readthedocs.io/en/latest/ 
* The random library https://docs.python.org/3/library/random.html
* Using delays is very important, but this could also be fixed using booleans which I would use for a longer program
