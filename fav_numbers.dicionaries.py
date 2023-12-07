#this programs is an example of how to use a dictionary

favorite_nums = {"anna":5, "sally":4, "julian":3, "mary":2, "rocky":1,}

print("This is the person-favorite number:")

print(favorite_nums)


print("\n\t*********** update ************\n")
#now each person can have more than one number and
#prints every fav number of each persone

fav_numbers = {
		"ana":[1,2,3],
		"sally":[4,5],
		"julia":[6,7,8],
		"mary":[9],
		"daniel":[10],
		}

for person, numbers in fav_numbers.items():
	print(f"{person.title()}'s favorite numbers:")
	for number in numbers:
		print(f"\t{number}.")
