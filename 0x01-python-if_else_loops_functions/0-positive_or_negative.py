#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	print(f"{}: is a positive number".format(number))
elif number == 0:
	print(f"{}: is zero".format(number))
else number < 0:
	print(f"{}: is a negative number".format(number))
