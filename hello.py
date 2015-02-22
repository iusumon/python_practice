import sys

args = sys.argv[1:]
args.reverse()
print(' '.join(args))


def hello():
    print("hello")

hello()

#import os
#os.system('/usr/bin/firefox')

fruits = ['apple', 'banana', 'orange']
upper_fruit = [fruit.upper() for fruit in fruits]
print(upper_fruit)


def fibo(n):
    fib_lst = [0, 1]
    for i in range(n):
        fib_lst.append(fib_lst[-1] + fib_lst[-2])

    return fib_lst


#my_fib_list = fibo(20)
#print(my_fib_list)


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(1000)


