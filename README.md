## SDSS Computing Studies Python Assignment
### Assignment #105 While vs For Loops (Total Marks 10)

Objectives:
* Identify when to use a while loop vs a for loop

For loops in Python are not like standard for loops in other programming languages.  In other programming languages, it is possible to reset a for loop from inside the for loop using a structure like the following:

```
for i in range(0,10):
    i = 4
    pass
```

You might think that this would constantly change the temporary/increment variable to 4, but it would never actually reach 10. However, this is not the case.  The range(0,10) statement creates a tuple: (0,1,2,3,4,5,6,7,8,9) and the for loop iterates through each member of the tuple.  Changing i to 4 within the loop doesn't affect the tuple, and it just proceeds to the next member of the tuple.

* A for loop in Python will only repeat a set number of times based on the list or tuple you are interating through and cannot be changed.

A while loop can have a variable number of iterations, because that number is set by the conditional statement that is being set by the while loop.  Consider the following infinite loop:

```
x = 0
while x != 3:
    x = 0
    print(f"x is {x}")
```

This loop will never exit because x is always not equal to 3.  We can have it mimic the behavior of a for loop by incrementing a counter.

```
i = 0
while i < 10:
    print(f"i is {i}")
    i = i + 1
```

Challenging Assignment:

Necklace Numbers
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with
Your program should do the following:
ask the user to enter in 2 digits.
Create the necklace number and display it:

example inputs: 
```
9 4 -> 94483257314595516742685494
1 3 -> 13472922461786527977538213
```


extra: What is the shortest necklace number sequence that can be made?

