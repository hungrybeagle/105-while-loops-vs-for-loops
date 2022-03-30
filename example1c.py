#! python3

"""
A better structure using a boolean variable!
Note that instead of storing whether the name is incorrect, we
are storing whether the name is correct.

In Python, the "not" is an acceptable way of checking to see if
a condition is not True, and sometimes makes more sense 
gramatically
"""
name = ""
correctName = False

while not correctName:
    name = input("Who is your favorite cartoon character?").strip()
    if name != "Marvin the Martian":
        print("  You can't be serious.")
    else:
        correctName = True

print("Marvin the Martian is my favorite character, too!")