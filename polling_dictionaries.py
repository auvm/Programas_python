dic_favorite_language = {"alex":"ruby", "mike":"pascal", "wozniak":"basic", 
			"dennis":"c", "ken":"go", "josh":"python", "linus":"c"}

for person, language in dic_favorite_language.items():
	print(
	f"Seem like {person.title()}'s favorite language is {language.title()}."
	)


list_people = ["mike", "josh", "mike", "dennis", "ken", "phillip", "elizabeth", "martha"]
print("People that should take the poll:")
for name in list_people:
	print(f"\t-{name}")

print("For that people...")
for name in list_people:
	if(name in dic_favorite_language.keys()):
		print(f"{name.title()}, thank you for answer the poll!")
	else:
		print(f"Dear {name.title()}, you should join us and answer the fucking poll.")


