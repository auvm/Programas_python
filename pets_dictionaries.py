#example, use differents dictionaries and strore them in a list to then, print
# everything about them

pet_1 = {"kind":"dog",
        "owner_name":"pedro",
        "age":4}

pet_2 = {"kind":"cat",
        "owner_name":"pablo",
        "age":2}

pet_3 = {"kind":"elephant",
        "owner_name":"mike",
        "age":23}

list_pet = [pet_1, pet_2, pet_3];

for pet in list_pet:
    pet_info = pet.items()
    print(f"{pet_info["owner_name"].title()} has a {pet_info["kind"]} like pet, and it is {pet_info["age"]}yo.")
