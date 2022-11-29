#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
stringNumber = str(number)
lastDigitOfNumber = int(stringNumber[len(stringNumber) - 1])
if number < 0:
    lastDigitOfNumber = -lastDigitOfNumber
print("Last digit of {:d} is {:d} ".format(number, lastDigitOfNumber), end='')
if 5 < lastDigitOfNumber:
    print("and is greater than 5")
elif 0 == lastDigitOfNumber:
    print("and is 0")
elif 6 > lastDigitOfNumber != 0:
    print("and is less than 6 and not 0")
