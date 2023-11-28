#!/usr/bin/python3
import random

def classify_number(number):
    if number > 0:
        return f"{number} is positive"
    elif number == 0:
        return f"{number} is zero"
    else:
        return f"{number} is negative"

def main():
    number = random.randint(-10, 10)
    result = classify_number(number)
    print(result)

if __name__ == "__main__":
    main()
