import random
import time

user_input = None

while user_input != "1" and user_input != "2":
    print("Welcome to NumberJuggle! If you would like to tell the computer what to do, press '1'.")
    user_input = input(print("If you would like the computer to tell you what operations to perform, press '2'. "))

if user_input == "1":

    max_num = 0.5
    while max_num % 1 != 0:
        max_num = input(print("Up to what number do you want the computer to pick? Please type an integer. "))
        max_num = float(max_num)
    max_num = int(max_num)

    total = random.randint(1, max_num)

    end_game = ""
    while end_game != "reveal":
        operation = None
        while operation != "add" and operation != "subtract" and operation != "multiply":
            operation = input(print("Would you like the add, subtract, or multiply? "))
            operation = operation.lower()

        number = 0.5 
        while number % 1 != 0:
            number = input(print("What number would you like computer to %s? Please enter an integer. " % operation))
            number = float(number)
        number = int(number)

        if operation == "add":
            total = total + number
            print("%sing %s..." % (operation , number))
        elif operation == "subtract":
            total = total - number
            print("%sing..." % operation)
        elif operation == "multiply":
            total = total * number
            print("%sing..." % operation)
        else:
            print("Something went wrong. ")

        time.sleep(3)

        print("If you would like the number to be revealed, type 'reveal'.")
        end_game = input(print("If you would like to continue, type anything else. "))
        end_game = end_game.lower()

    
