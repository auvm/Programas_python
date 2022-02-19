# Angel Uriel Velasco Mejía
# 10/01/2022
# This file contains little exercises of the chapter 2
# of python crash course, using strings, and funtions 
# to manages them, make them upper, lower an title text.
# I play whit the print formated output too.

name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

print("This is upper case: "+name.upper()+"\n"+
    "This is lower case: "+name.lower()+"\n"+
    "This is title case: "+ name.title())

name = "Alber Einstein"
message = "A person who never made a mistake never tried anything new."

print(f"{name} once said, \"{message}\"\n")

name = "\tAlber Einstein\t"
print("A rare input: \n***"+name+"***")
print("Without left spaces: ***"+name.lstrip()+"***")
print("Without right spaces: ***"+name.rstrip()+"***")
print("Without spaces both sides: ***"+name.strip()+"***")