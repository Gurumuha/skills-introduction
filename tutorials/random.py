import random
num1 =random.randint(1,100)

while True:
    try:
        choice =int(input("Enter a number between 1 and 100: "))
        if choice == num1:
            print("You guessed the correct number!")
            break
        elif choice > num1:
            print("Too high!")
        elif choice < num1:
            print("Too low!")
        elif choice ==0 or choice >100:
            print("Number outside range!")
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter a valid number:")

