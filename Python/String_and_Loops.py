input = str(input("Enter your phrase: "))
input = input.replace(" ", "-") 
letter_list = list(input) 
print(*letter_list, sep='\n') 
