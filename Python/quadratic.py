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

