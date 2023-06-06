#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDeg = -(-number % 10) if number < 0 else (number % 10)
if lastDeg > 5:
    print(f"Last digit of {number} is {lastDeg} and is greater than 5")
elif lastDeg == 0:
    print(f"Last digit of {number} is {lastDeg} and is 0")
else:
    print(f"Last digit of {number} is {lastDeg} and is less than 6 and not 0")
