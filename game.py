import random

def main():
    
    #hint
    
    H = random.randint(0, 5)
    Hint = pc - H or pc + H
    print("Hint is.......",Hint)
    
    number = random.randint(10, 100)
    user_input = int(input("Enter a number between 10-100: "))
    
    #conditions for winning or losing.
    
    if user_input == number:
        print("You just won!")
    elif user_input > number:
        print("Higher!")
    elif user_input < number:
        print("Lower!")
    elif user_input < 10:
        print("Choose above 10!")
    elif user_input > 100:
        print("Choose upto 100!")
    else:
        print("Number was",number)

#Again        
        
def again():
    user_input = input("Play again?: ")
    if user_input == "yes" or "Yes":
        main()
        again()
    else:
        print("Goodbye!")
main()
again()
