'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# common_num = list(set(a).intersection(set(b)))
# print common_num

# print(list(set(a) & set(b)))
c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
#
# print c

# print list(set([i for i in a if i in b]))

commonList = list(set([i for i in a for j in b if i == j]))
print(commonList)


a = [random.randrange(1, 9) for i in range(10)]
b = [random.randrange(1, 11) for i in range(10)]
c = set(i for i in a if i in b)
print(c)
