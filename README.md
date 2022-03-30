## SDSS Computing Studies Python Assignment
### Assignment #004c While Loops (Total Marks 10)

Objectives:
* To repeat a loop until a boolean condition is met
* Break out of while loops to prevent infinite loops

There are times when you might want to keep repeating a block of
code endlessly until a specific condition is met.  For example,
you might want to allow a user unlimited opportunities to try
guessing their password and deny them access until they get it
right, or until they reach a specific number of attempts.
Another time you might want to repeat a block of code endlessly
is if you're trying to repeat a number of steps, but don't know
how many steps are going to be taken.  An example might be in a
number guessing game.  You might want people to keep guessing
until they have reached the correct number.

A while loop checks a condition, and if the condition is True,
it executes the block of code, and will keep doing so until the
condition is False

Sometimes, however, you might need to program in a "failsafe",
a way to break out of the program if it looks like the condition
might never be False.  Then the "break" command can be used.

Look at the example programs to see how a While loop operates.

### 3 Tasks, 3 Problems, 12 marks

##### Task 1
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)

##### Task 2
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

##### Task 3
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)

##### Problem 1
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

##### Problem 2
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

##### Problem 3
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:

Example:
1 1 2 3 5
(2 points) 

