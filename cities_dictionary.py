#list of cities with some info about it

dic_cities = {
                "Paris":{
                    "country":"francia",
                    "population": 182000,
                    "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    },
                "ciudad de mexico":{
                    "country":"mexico",
                    "population": 1128000,
                    "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    },
                "new york":{
                    "country":"USA",
                    "population": 238000,
                    "info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                }
             }

for city, info in dic_cities.items():
    print(f"{city.title()}:")
    for field, val in info.items():
        print(f"\t{field.title()}: {val}.")
    
    
    