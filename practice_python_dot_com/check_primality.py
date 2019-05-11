'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
'''

def check_primality(user_number):
    is_prime = True
    for i in range(user_number):
        print(i)
        # if i == user_number or i == 1:
            # continue
        if user_number % 2 == 0:
            is_prime = False
            return is_prime
    return is_prime

user_num = int(input("Enter a number to check primality: "))

# print(check_primality(user_num))

if check_primality(user_num) == True:
    print("The number " + str(user_num) + " is a prime one.")
else:
    print("The number " + str(user_num) + " is not a prime one.")
