#auvm 27/06/2022
#using at least one funtion 
# of this chapter

from audioop import reverse
from pickle import TRUE

#I only used insert metods to remember
#them
cities = ["los angeles", "mexico", "santa fe",
"albuquerque","new new york", "boston"]
print(cities)
cities.append("chihuahua")
print(cities)
cities[4] = "new york"
cities.remove("mexico")
print(cities)
cities.insert(0, "tampa")
print(cities)
print(sorted(cities))
print(sorted(cities,reverse=True))
print(cities)
cities.reverse()
print(cities)