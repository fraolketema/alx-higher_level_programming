#!/usr/bin/python3
import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero")
        sys.exit(1)

if __name__ == "__main__":
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    except ValueError:
        print("Error: Please provide valid integer arguments.")
        sys.exit(1)

    result = operators[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
