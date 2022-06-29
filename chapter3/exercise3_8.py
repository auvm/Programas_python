# auv, 27/06/2022
# demonstration of using sorting methods

from pyrsistent import v


places_to_visit = ["paris", "china", "moscow", "japan", "mexico"]

#original order
print("orignal = ", places_to_visit)
#alphabetical order
print("alphabetical order = ", sorted(places_to_visit))
#original order
print("orignal = ", places_to_visit)
#reverse alphabetical order
print("reverse alphabetical order = ", sorted(places_to_visit, reverse=True))
#original order
print("orignal = ", places_to_visit)
#reverse order
places_to_visit.reverse()
print("reverse original order = ", places_to_visit)
#reverse to original order
places_to_visit.reverse()
print("reverse to the original order= ", places_to_visit)
#permanent alphabetical order
places_to_visit.sort()
print("permant alphabetical order= ", places_to_visit)
#permanent alphabetical order
places_to_visit.sort(reverse=True)
print("reverse permant alphabetical order= ", places_to_visit)