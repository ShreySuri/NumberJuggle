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
    original_num = total

    end_game = ""
    turn_count = 0
    while end_game != "reveal":

        operation = None
        while operation != "add" and operation != "subtract" and operation != "multiply":
            print("")
            operation = input(print("Would you like to add, subtract, or multiply? "))
            operation = operation.lower()

        number = 0.5 
        while number % 1 != 0:
            print("")
            number = input(print("What number would you like the computer to %s? Please enter an integer. " % operation))
            number = float(number)
        number = int(number)

        print("")
        
        if operation == "add":
            total = total + number
            print("%sing %s..." % (operation , number))
        elif operation == "subtract":
            total = total - number
            print("%sing %s..." % (operation , number))
        elif operation == "multiply":
            total = total * number
            print("%sing by %s..." % (operation , number))
        else:
            print("Something went wrong. ")

        time.sleep(3)

        print("")
        print("If you would like the number to be revealed, type 'reveal'.")
        end_game = input(print("If you would like to continue, type anything else. "))
        end_game = end_game.lower()
        turn_count = turn_count + 1

        if turn_count < 3 and end_game == "reveal":
            print("")
            print("Are you sure you want the total to be revealed? Maybe a few more turns?")
            final = input(print("Type 'yes' or 'no'"))
            final = final.lower()
            if final == "yes":
                end_game = "reveal"
            else:
                end_game = ""

    print("")
    print("The final total is %s, over the course of %s turns." % (total, turn_count))

    guess = 0.5
    while guess % 1 != 0:
        print("")
        guess = input(print("Enter what you think the original number was. Please enter an integer. "))
        guess = float(guess)
    guess = int(guess)

    print("")
    
    if guess == original_num:
        print("You got it! If you would like to be challenged more, increase the max number next time you play.")
    else:
        print("Sorry, the original number was %s. You can lower the difficulty by decreasing the max number the next time you play.") 
