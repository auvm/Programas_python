person1 = {'first':'paco', 'last':'martinez', 'age':31, 'city':'new york'}
person2 = {'first':'miguel', 'last':'diaz', 'age':24, 'city':'rusia'}
person3 = {'first':'angel', 'last':'velasco', 'age':23, 'city':'mexico'}

list_people = [person1, person2, person3]

#printing everything i know about the people
for person in list_people:
    print(f"{person['first'].title()} {person['last'].title()} is {person['age']} yo and lives in {person['city'].title()}.")