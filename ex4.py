"""Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. (If you don’t know what a divisor is, it is a number
that divides evenly into another number. For example, 13 is a divisor of 26 because
26 / 13 has no remainder.)"""

num = int(input("Please enter a number: "))
newlist = []
for x in range(1, num+1): # because it will exclude the max number
    if num%x == 0: # seeing if our max number can divide all other numbers in our range
        newlist.append(x)

print(newlist)
