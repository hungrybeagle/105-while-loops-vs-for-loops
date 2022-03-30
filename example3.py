#! python3

"""
Sometimes you might run the risk of an infinite loop.
It is helpful to build in a failsafe to break out of the
loop using the break command, or terminate your program
using the exit() command
"""
import time
import random

count = 0

while True:
    #random.random() creates a random value between 0 and 1
    print("This will be an infinite loop!")
    delay = random.random() + 1
    count = count + 1
    if count > 50:
        break

print("We broke out of an infinite loop by using the break command")
    