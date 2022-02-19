guests = ["john lennon", "emiliano zapata", "porfirio díaz"]
print(f"Hi {guests[0].title()} I invite you to my dinner.")
print(f"Hi {guests[1].title()} I invite you to my dinner.")
print(f"Hi {guests[2].title()} I invite you to my dinner.")
print("\n\t**************\t**************\n")
print(f"Oh No! {guests[2].title()} won't come to my dinner.")

guests[2] = "tyler joseph"

print("But wait, I found a bigger table avalible")

guests.insert(0,"david muray")
guests.insert(2,"joseph stalin")
guests.insert(4,"hirohito")

print(f"Now I'll invite to {guests[0].title()} to my diner.")
print(f"to {guests[2].title()} and {guests[4].title()}.")
print("\n\t**************\t**************\n")
print("Sorry guy, but that mother fuker of Benson take me off again, so...")
lastOne=guests.pop()
print(f"{lastOne.title()}, you can't come to my dinner, sorry.")
lastOne=guests.pop()
print(f"{lastOne.title()}, you can't come to my dinner too, sorry.")
lastOne=guests.pop()
print(f"{lastOne.title()}, you can't come to my dinner too, sorry.")
lastOne=guests.pop()
print(f"{lastOne.title()}, you can't come to my dinner too, sorry.")
print("\n\t**************\t**************\n")
print(f"Well, {guests[-1].title()} you're still invited")
print(f"{guests[-2].title()} you're still invited too.")
print("\n\t**************\t**************\n")
print("Well, till the next time!")

del guests[-1]
del guests[-1]

print(guests)