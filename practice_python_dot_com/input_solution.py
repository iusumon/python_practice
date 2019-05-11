'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
'''

name = input("What is your name: ")
age = input("Age: ")
year = 2016- int(age) + 100
print(name + " will be 99 years old in the year " + str(year))
