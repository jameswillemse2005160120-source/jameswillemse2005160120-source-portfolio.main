# 6-7. People
# Create three dictionaries representing different people
person1 = {
    'first_name': 'Lerato',
    'last_name': 'Mokoena',
    'age': 18,
    'city': 'Johannesburg'
}

person2 = {
    'first_name': 'Thabo',
    'last_name': 'Nkosi',
    'age': 22,
    'city': 'Pretoria'
}

person3 = {
    'first_name': 'Aisha',
    'last_name': 'Khan',
    'age': 20,
    'city': 'Cape Town'
}

# Store all people in a list
people = [person1, person2, person3]

print("👥 People Information:")
for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")

# 6-8. Pets
# Create dictionaries for different pets
pet1 = {'animal': 'dog', 'owner': 'James'}
pet2 = {'animal': 'cat', 'owner': 'Zanele'}
pet3 = {'animal': 'parrot', 'owner': 'Neo'}

# Store pets in a list
pets = [pet1, pet2, pet3]

print("🐾 Pet Information:")
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}\n")

# 6-9. Favorite Places
favorite_places = {
    'James': ['Cape Town', 'Durban', 'Kruger National Park'],
    'Thabo': ['Drakensberg', 'Soweto'],
    'Aisha': ['Garden Route', 'Stellenbosch']
}

print("📍 Favorite Places:")
for name, places in favorite_places.items():
    print(f"{name}'s favorite places:")
    for place in places:
        print(f" - {place}")
    print()

# 6-10. Favorite Numbers (multiple numbers per person)
favorite_numbers = {
    'James': [7, 14],
    'Thabo': [3, 6, 9],
    'Aisha': [11, 22],
    'Zanele': [5],
    'Neo': [9, 18]
}

print("🔢 Favorite Numbers (Multiple):")
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers:")
    for number in numbers:
        print(f" - {number}")
    print()

# 6-11. Cities
cities = {
    'Johannesburg': {
        'country': 'South Africa',
        'population': '5.6 million',
        'fact': 'It is the largest city in South Africa and a major economic hub.'
    },
    'Cape Town': {
        'country': 'South Africa',
        'population': '4.6 million',
        'fact': 'Known for Table Mountain and beautiful beaches.'
    },
    'Durban': {
        'country': 'South Africa',
        'population': '3.4 million',
        'fact': 'Has one of the busiest ports in Africa.'
    }
}

print("🌆 City Information:")
for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")

# 6-12. Extensions
# Let's extend the 'people' program by adding hobbies and formatting it better
person1['hobby'] = 'Photography'
person2['hobby'] = 'Cycling'
person3['hobby'] = 'Painting'

print("🎨 Extended People Information with Hobbies:")
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Name: {full_name}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print(f"Hobby: {person['hobby']}\n")