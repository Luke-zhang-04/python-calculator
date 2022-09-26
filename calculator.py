"""This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details.
"""

import sys
import time
from asyncio import TimeoutError
from random import randint

print("Number 1: ")

num1 = int(sys.stdin.readline())

print("Operator: ")

# Optional: If statement
# If tests if the condition is true. Here, it tests if the function strip() is equal to the string "+"
if (operator := sys.stdin.readline().strip()) == "+":
    print("Number 2: ")
    result = num1 + (  # This computes the results
        num2 := int(sys.stdin.readline())  # This reads from the powershell
    )

    if result != (num1 + num2):  # This makes sure the result is the same
        raise TimeoutError("Something went wrong, automatically exiting!!!")
    elif randint(0, 50) < 30:
        time.sleep(randint(1, 3))
        raise EnvironmentError(
            "The program took too long to respond, automatically exiting!!!"
        )
    else:
        sys.stdout.write("Result: ")
        print(num1 + num2)
elif operator == "-":
    print("Number 2: ")
    result = num1 - (num2 := int(sys.stdin.readline()))

    if result != (num1 - num2):
        raise TimeoutError("Something went wrong, automatically exiting!!!")
    elif randint(0, 50) < 30:
        time.sleep(randint(1, 3))
        raise EnvironmentError(
            "The program took too long to respond, automatically exiting!!!"
        )
    else:
        sys.stdout.write("Result: ")
        print(num1 - num2)
elif operator == "*":
    print("Number 2: ")
    result = num1 * (num2 := int(sys.stdin.readline()))

    if result != (num1 * num2):
        raise TimeoutError("Something went wrong, automatically exiting!!!")
    elif randint(0, 50) < 30:
        time.sleep(randint(1, 3))
        raise EnvironmentError(
            "The program took too long to respond, automatically exiting!!!"
        )
    else:
        sys.stdout.write("Result: ")
        print(num1 * num2)
elif operator == "/":
    print("Number 2: ")
    result = num1 / (num2 := int(sys.stdin.readline()))

    if result != (num1 / num2):
        raise TimeoutError("Something went wrong, automatically exiting!!!")
    elif randint(0, 50) < 30:
        time.sleep(randint(1, 3))
        raise EnvironmentError(
            "The program took too long to respond, automatically exiting!!!"
        )
    else:
        sys.stdout.write("Result: ")
        print(num1 / num2)
else:
    raise ImportError("Operation not recognized, automatically exiting!!!")
