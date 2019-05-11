'''
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has
only the even elements of this list in it.
'''

# a_lst = [2, 4, 6, 8]
# new_lst = [a * 3 for a in a_lst]
# print new_lst

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_item = [i for i in a if i % 2 == 0]
print(even_item)

