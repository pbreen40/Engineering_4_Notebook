# Quadratic Solver
# Written by Philip
import math 
def doMath(a,b,c): #Function used to do the math which is called in the prints
    if(-4*a*c>b*b):
        discrimin = (math.sqrt(b*b-4*a*c)) 
        root1= (-b +discrimin)/a
        root2= (-b -discrimin)/a
        roots = [root1,root2]
        return(roots)       
    


while True:
    # Take input from the user
  

    
        print("Quadratic Solver")
        print("Enter the coefficients for ax^2 + bx + c = 0")
        a = int(input("Enter a: "))#Gathers first number   
        b = int(input("Enter b: "))#gathers second number
        c = int(input("Enter c: "))
        print("Roots:", doMath(a,b,c))
        
        
        break #ends code

