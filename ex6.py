"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

w1 = input("Please input a string, I will tell you if it's a palindrome or not!")
w2 = w1[::-1] # reads the string from the first index to the last index in reverse order
if w1==w2:
    print("String is palindrome")
else:
    print("String is not a palindrome")