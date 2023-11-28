#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ls = abs(number) % 10 * (-1 if number < 0 else 1)

if ls > 5:
    print(f"Last digit of {number} is {ls} and is greater than 5")
elif ls == 0:
    print(f"Last digit of {number} is {ls} and is 0")
else:
    print(f"Last digit of {number} is {ls} and is less than 6 and not 0")
