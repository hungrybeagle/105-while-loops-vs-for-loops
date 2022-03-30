#! python3

"""
This uses the same basic program as example 1, but uses a boolean variable in
the while loop structure.
incorrectName is set to True (the name is incorrect) so the while loop
will continue to run until the incorrectName is False (a double negative!)
"""
name = ""
incorrectName = True
while incorrectName:
    name = input("Who is your favorite cartoon character?").strip()
    if name != "Marvin the Martian":
        print("  You can't be serious.")
    else:
        incorrectName = False

print("Marvin the Martian is my favorite character, too!")