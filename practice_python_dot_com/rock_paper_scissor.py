'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

#1st Solution
#=================================================
# rules = '\nr = rock\np = paper\ns = scissors'
# play = 'y'
#
# wins = {
#     'r' : 's',
#     'p' : 'r',
#     's' : 'p',
# }
#
#
# def result(a, b):
#     if a == b:
#         return 'Tie!'
#     elif wins[a] == b:
#         return 'A wins'
#     else:
#         return 'B wins!'
#
#
# while play == 'y':
#     print(rules)
#     a = input('\nYour move, A: ')
#     b = input('\nYour move, B: ')
#     play = input('\n' + result(a, b) + ' play again? (y/n) ')


#2nd Solution
#=================================================

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()


print(compare(user1_answer, user2_answer))
