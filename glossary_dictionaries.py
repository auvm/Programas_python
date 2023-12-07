#print a word with its meaning using a dictionary

words = {"loop":"cicle of something, normally a program o part of a program.",
         "if":"reserved word for a conditional funtion, followed by the condition of the program itseft.",
         "list":"data programming structured use to store any kind of objects from a programming language.",
         "tuple":"similar data storing structured as a list, but it is immutable, so any elements can change during the execution.",
         }

print(f"""
loop:\n\t{words["loop"].title()}
if:\n\t{words["if"].title()}
list:\n\t{words["list"].title()}
tuple:\n\t{words["tuple"].title()}
""")
