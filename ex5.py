"""  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# Randomly generate two lists
import random
randomA = random.sample(range(0, 100), 10)
randomB = random.sample(range(0, 100), 15)
print(randomA)
print(randomB)

commonelements = []
for element in randomA:
    if element in randomB:
        if element not in commonelements: # this helps you eliminate duplicates. For each loop iteration, it will see if the number is already there. If it is, it will not append
            commonelements.append(element)
print(commonelements)

# Print in one line of python: Using set method
print(list(set(a).intersection(b)))
print(list(set(randomA).intersection(randomB)))
