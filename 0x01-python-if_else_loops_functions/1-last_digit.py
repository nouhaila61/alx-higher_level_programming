#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDegit = -(-number % 10) if number < 0 else (number % 10)
if lastDegit > 5:
    print(f"Last digit of {number} is {lastDegit} and is greater than 5")
elif lastDegit == 0:
    print(f"Last digit of {number} is {lastDegit} and is 0")
else:
    print(f"Last digit of {number} is {lastDegit} and is less than 6 and not 0")
