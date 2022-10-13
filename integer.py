#!/usr/bin/env python3
# Created By: Daniel Momoh
# Date: Oct 11th, 2022
# This asks the user to enter an integer
# it then determines if the integer is positive or negative


n = float(input("Input a number: "))
if n >= 0:
    if n == 0:
        print("It is Zero!")
    else:
        print("Number is Positive number.")
else:
    print("Number is Negative number.")
