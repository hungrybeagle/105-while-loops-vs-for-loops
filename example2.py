#!python3

"""
While statements can update the condition variables without input 
from the user as well
"""

# This program will try to get closer and closer to a number
# until it is "close enough" (less than 1 unit from the actual number)
# it uses new modules: random and time

import random
import math
import time

#random.randint creates a random integer that includes the beginning and ending values
targetNum = random.randint(1,100)
guess = 50
count = 0

print("The target is " + str(targetNum))
print("===================")
while targetNum != guess:
    print(guess)
    difference = guess - targetNum
    guess = guess - math.ceil(difference / 2)
    count = count + 1
    # time.sleep(x) will pause the program at this point for x seconds where x is a float 
    time.sleep(1)
print("===================")
print("I took " + str(count) + " repetitions to find the number was " + str(guess))