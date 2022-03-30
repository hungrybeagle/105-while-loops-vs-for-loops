#! python3

"""
we are going to be checking the value of the variable "name"
before we have input that creates it, so we should create
a variable with no contents otherwise the conditional statement
might throw an error stating that the variable does not exist
"""
name = ""

while name != "Marvin the Martian":
    name = input("Who is your favorite cartoon character?").strip()
    if name != "Marvin the Martian":
        print("  You can't be serious.")

print("Marvin the Martian is my favorite character, too!")