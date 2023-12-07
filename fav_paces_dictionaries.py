#crea un diccionario con con nombres de personas donde guarda al menos 3
#lugares favoritos que tienen en una lista

fav_places = {
		"angel":["parking lot", "park", "the office"],
		"martha":["dentist", "school", "desert"],
		"daniel":["the crew", "school", "library"],
		"david":["park", "kitchen", "mall"]
	     }

for person, places in fav_places.items():
	print(f"Favorite places of {person.title()}:")
	for place in places:
		print(f"\t*{place.title()}")
