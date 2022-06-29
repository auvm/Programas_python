my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
i = 1
for food in my_foods:
    print(f"{i}.- {food.title()}")
    i+=1
print("\nMy friend's favorite foods are:")
i = 1
for food in friend_foods:
    print(f"{i}.- {food.title()}")
    i+=1