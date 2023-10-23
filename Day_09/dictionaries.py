programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
programming_dictionary = {}
print(programming_dictionary)

travel_vlog = {
    'France': {
        'cities_visited': ['paris', 'Lille', 'Dijon']
    }
}

travel_vlog = [
    {
        'country': 'France', 
        'cities_visited': ['paris', 'Lille', 'Dijon'], 
        'total_visits': 12
    },
    {
        'country': 'Germany', 
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 
        'total_visits': 5
    },
]

print(travel_vlog[1]['cities_visited'])