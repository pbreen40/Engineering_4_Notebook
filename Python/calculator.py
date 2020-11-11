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

