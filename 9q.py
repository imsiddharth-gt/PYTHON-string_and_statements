""" Check whether a number is an Armstrong number."""

num = (input("Enter a number " ))

if int(num[0])**3 + int(num[1])**3 + int(num[2])**3 == int(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")