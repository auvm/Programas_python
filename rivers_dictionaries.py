#imprime tres nombres de rios y el país donde fluye

dic_rivers = {"canada":"mackenzie","usa":"misuri","mexico":"conchos"}


#el método items devuelve en la primer variable la key, luego el value
for country, river in dic_rivers.items():
	print(f"El río {river.title()} fluye através de {country.title()}.");

print("\nTodos los ríos:")
for river in dic_rivers.values():
	print(river.title());

print("\nTodos los países:")
for country in dic_rivers.keys():
	print(country.title());
