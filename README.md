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
#import pyautogui 
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
    if keyboard.is_pressed('enter'): #I'm using a keyboard libray but I also found pyautogui which is a cool little tool I found that is helpful
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


### Calculator 

#### Assignment:
Write a program that gives you the sum, difference, quotient, and modulo of the two numbers.  The program asks the user for two numbers and then runs them through one function, five different times. 

#### Code:
```python
# Calculator 
# Written by Philip

def doMath(x,y,z): #Function used to do the math which is called in the prints
    if(z==1):#addition
        return x + y
    if(z==2):#subtraction
         return x - y
    if(z==3):#mulitplication
         return x * y
    if(z==4):#division
         return round(x / y, 2)#rounds to 2 decimal places
    if(z==5):#modulo
         return x % y

while True:
    # Take input from the user
  

    
    
        x = float(input("Enter first number: "))#Gathers first number   
        y = float(input("Enter second number: "))#gathers second number

        print("Sum:        ", doMath(x,y,1))#calls doMath function with 3 sets of data, first 2 give it the numbers the user enters, third specifies which operation to do
        print("Difference: ", doMath(x,y,2))
        print("Product:    ", doMath(x,y,3))
        print("Quotient:   ", doMath(x,y,4))
        print("Modulo:     ", doMath(x,y,5))
        break #ends code
```
#### What to Remember:
* Use variable = input(PRINT STATEMENT) to take an input from the user
* Use 115200 as the speed for PuTTY SSH
* Shift + INS will paste into the SSH
* You can give a function as many numbers or variables you want when you call it, as long as you define those variables when you create the function
* Using return will return data to where ever you called the function

### Quadratic Solver

#### Assignment:
Write a simple program that solves quadratic functions.
 

#### Code:
```python
# Quadratic Solver
# Written by Philip
import math 
def doMath(a,b,c): #Function used to do the math which is called in the prints
    if(-4*a*c>b*b): #checks if the discriminant will be negative
        discrimin = (math.sqrt(b*b-4*a*c)) #if not it get its
        root1= (-b +discrimin)/a #finds the roots using quadratic formula
        root2= (-b -discrimin)/a
        roots = [root1,root2]#creates root array
        return(roots)     #returns roots
    


while True:
    # Take input from the user
  

    
        print("Quadratic Solver")
        print("Enter the coefficients for ax^2 + bx + c = 0")
        a = int(input("Enter a: "))#Gathers first number   
        b = int(input("Enter b: "))#gathers second number
        c = int(input("Enter c: "))#gathers third number
        print("Roots:", doMath(a,b,c))#returns Roots: None if no roots, but returns the roots if there are some
        
        
        break #ends code
```
#### What to Remember:
* Arrays can be super helpful, espescially when dealing with multiple numbers that are all related. 
* You can return an array

### Strings and Loops

#### Assignment:
Write a program that recieves an input from a user and splits each character into a line and prints it out.
 

#### Code:
```python
input = str(input("Enter your phrase: "))
input = input.replace(" ", "-") 
letter_list = list(input) 
print(*letter_list, sep='\n') 
```
#### What to Remember:
* Use sep='\n' to seperate each line in a list
* Use input.replace("x", "y") to replace characters in a list 

### Hangman

#### Assignment:
Write a program that lets the user play hangman with a computer!
 

#### Code:


```python
import random
health = 5 #amount of health
letterInput = " "
word = ["swag", "litty", "keyboard", "mouse", "water", "computer", "python"]#words that can be chosen 
answer = word[random.randint(0,len(word)-1)]#picks a word randomly
answers = []#guesses
win = None#used to end game if they won/lost
guess = 0#correct guesses
letter=len(set(answer))
for x in range(len(answer)):
    answers.extend('_') 
print("Hangman")

def hangman(health):   #function that prints out the body(depressing)
    if health==0:
        print("---┐")
    if health==1:
        print("---┐")
        print("   O")
    if health==2:
        print("---┐")
        print("   O")
        print("   |")
    if health==3:
        print("---┐")
        print("   O")
        print("   |")
        print(" --|--")
    if health==4:
        print("---┐")
        print("   O")
        print("   |")
        print(" --|--")
        print("   |")
    if health==5:
        print("---┐")
        print("   O")
        print("   |")
        print(" --|--")
        print("   |")
        print("  | |")


while health>0: #while alive
    letterInput = input("Guess: ")#asks for guess
    if letterInput in answer:#checks if its in the answer
        print("Correct!")
        for x in range(len(answer)):
            if letterInput == answer[x]:
                answers[x] = letterInput
        print(answers)
        guess = guess + 1
        if guess == letter:#if amount of right guesses=amount of possible right guesses you win
            win = True
            break
    else:   
        health = health-1#subtracts health and asks to try again
        print("Incorrect, try again")
        print("You have " + str(health) + " health")
        hangman(health)

if win == True:
    print("GG You Won!")
else:
    print("You Lost :(")
```

#### What to Remember:
* Functions can be super useful, this was an example of that
* Make sure you always double check your code after making a minor or major change so you know it still works and can fix it now rather than down the line

### Bash GPIO Pins

#### Assignment:
Use a bash script to make two LEDs blink on and off 10 times.
 

#### Code:


```python
gpio mode 1 out
gpio mode 0 out
for (( c=0; c<=9; c++ ))
do  
   gpio write 1 1   
   gpio write 0 1
   sleep .5
   gpio write 1 0
   gpio write 0 0
   sleep .5
done
```

#### What to Remember:
* Doing research to fix your problems is very important
* You can just turn on a pin and tap the LEDs wire to find it(Thanks Vann)



### Python GPIO Pins

#### Assignment:
Use a python script to make two LEDs blink on and off 10 times.
 

#### Code:


```python
  
import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) # Everything breaks when this is removed
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Pin 8 is an output
for x in range(10):   #loop runs 10 times
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
```

#### What to Remember:
* https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/ Was very helpful
* You can just use one pin and plug the LEDs into the bus!


### GPIO Pins SSH

#### Assignment:
Use SSH to remotely control LEDs.
 


#### What to Remember:
* This is really really cool, it felt so cool to be controlled the light from across my house. 
* I had to make sure I took a picture of my Pis IP in case I lost it.

### GPIO Pins I2C

#### Assignment:
Use an accelerometer to gather acceleration data and display it on an OLED display.
 

#### Code:

```python
import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24 
accelerometer = Adafruit_LSM303.LSM303() # setting up accelerometer
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) # setting up display
disp.begin() #starting display, clearing display
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) 
draw.rectangle((0,0,width,height), outline=0, fill=0) # clears screen


padding = 3
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default() 



while True:   
	accel, mag = accelerometer.read() # gathers accelerometer data
	accel_x, accel_y, accel_z = accel 
	
	

	draw.text((x, top), "Accelerometer Data:", font=font, fill=255) 
	draw.text((x, top + 10), "Accel x ={0}".format(round(accel_x / 100, 3)), font=font, fill=255) # prints x 
	draw.text((x, top + 20), "Accel y ={0}".format(round(accel_y / 100, 3)), font=font, fill=255) # prints y
	draw.text((x, top + 30), "Accel z ={0}".format(round(accel_z / 100, 3)), font=font, fill=255) # prints z
	
	
	disp.image(image) 
	disp.display()

	
	draw.rectangle((100, 12, 55, 50), outline=0, fill=0) 
	disp.image(image)
	disp.display()

	#sleep for debug, I've found it to be useful in the past
	time.sleep(.15)```
#### What to Remember:
* Delays are super important for debugging or even to get your code to work.
* The PI will throw errors if there is any faulty wiring
