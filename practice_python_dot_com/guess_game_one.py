'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or
exactly right. (Hint: remember to use the user input lessons from the very
first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random
num_generated = random.randint(0, 9)

run_again = "y"

while run_again == 'y':
    user_input = input("Enter a number of your guess: ")
    if int(user_input) > num_generated:
        print("Your guess was high")
    elif int(user_input) < num_generated:
        print("Your guess was low")
    else:
        print("Your guess is equal to computer")
    run_again = input("Do you want to run again(y/n): ")

