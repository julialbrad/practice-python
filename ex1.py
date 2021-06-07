"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year
that they will turn 100 years old.
"""

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
turn100 = 2021 + (100 - age)
statement = (name+ ', You will turn 100 in the year ' + str(turn100))
print(statement)

"""Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)"""

repeats = int(input('Please enter the number of times you\'d like to repeat the previous statement: '))
i = 0
while i < repeats:
    print(statement)
    i += 1
