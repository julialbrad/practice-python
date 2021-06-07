"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

num = int(input('Please enter a number: '))
check = int(input('Please enter another number: '))

if num%2 == 0 and num%4 == 0:
    print("Your first number is even and a multiple of 4")
elif num%2 == 0 and num%4 != 0:
    print("Your number is even")
else:
     print("Your number is odd")

if num%check == 0:
    print("Your second number divides evenly into the first")
else:
    print("Your second number does not divide evenly into the first")
