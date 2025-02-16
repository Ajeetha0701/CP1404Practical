import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


"""
line 1: 13, 
# the smallest number: 5
# the largest number: 20

line 2: 7,
# the smallest number: 3
# the largest number: 9

line 3 : 3.0824,
# the smallest number: 2.5
# the largest number: 5.5
"""
print(random.uniform(1, 100))
