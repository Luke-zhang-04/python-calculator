"""Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
OF THIS SOFTWARE.
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
