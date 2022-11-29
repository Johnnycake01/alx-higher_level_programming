#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
stringNumber = str(number)
lastDigitOfNumber = int(stringNumber[len(stringNumber) - 1])
comment = ""
if lastDigitOfNumber > 5:
    comment = "and is greater than 5"
elif lastDigitOfNumber == 0:
    comment = "and is 0"
elif lastDigitOfNumber < 6 and lastDigitOfNumber != 0:
    comment = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, lastDigitOfNumber, comment))
