from cgi import print_form


favorite_pizzas = ["Peperoni", "Hawaiana", "Mexicana"]
for type_pizza in favorite_pizzas:
    print(f"I like {type_pizza} pizza.")

print(f"{favorite_pizzas[0]}, {favorite_pizzas[1]}, {favorite_pizzas[2]}, I really love pizza!")

friend_pizzas = favorite_pizzas[:]

print(f"""He like {friend_pizzas[0]}, {friend_pizzas[1]}
    and {friend_pizzas[2]} pizzas too.""")

friend_pizzas.append("Carne")

print(f"But he also like the {friend_pizzas[-1]} pizzas.\nHere is the complete list of us:")

print("Mine:")
for type_pizza in favorite_pizzas:
    print(type_pizza)
print("His:")
for type_pizza in friend_pizzas:
    print(type_pizza)

