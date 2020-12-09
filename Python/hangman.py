import random
health = 5
letterInput = " "
word = ["swag", "litty", "keyboard", "mouse", "water", "computer", "python"]
answer = word[random.randint(0,len(word)-1)]
answers = []
win = None
guess = 0
letter=len(set(answer))
for x in range(len(answer)):
    answers.extend('_') 
print("Hangman")

def hangman(health):   #this is the array of the hangman drawings
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


while health>0:
    letterInput = input("Guess: ")
    if letterInput in answer:
        print("Correct!")
        for x in range(len(answer)):
            if letterInput == answer[x]:
                answers[x] = letterInput
        print(answers)
        guess = guess + 1
        if guess == letter:
            win = True
            break
    else:   
        health = health-1
        print("Incorrect, try again")
        print("You have " + str(health) + " health")
        hangman(health)

if win == True:
    print("GG You Won!")
else:
    print("You Lost :(")
