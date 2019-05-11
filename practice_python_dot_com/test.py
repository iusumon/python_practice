import random
# a = [random.randrange(1, 9) for i in range(10)]
# b = [random.randrange(1, 11) for i in range(10)]
a = random.sample(range(0, 30), 9)
b = random.sample(range(1, 20), 9)
c = list(set(i for i in a if i in b))
print(c)
