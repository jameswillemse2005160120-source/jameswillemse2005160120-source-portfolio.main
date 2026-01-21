# 6-1. Person
person = {
    'first_name': 'Lerato',
    'last_name': 'Mokoena',
    'age': 18,
    'city': 'Johannesburg'
}

print("Person Information:")
print("First Name:", person['first_name'])
print("Last Name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])
print("\n")  # Adds a blank line for readability

# 6-2. Favorite Numbers
favorite_numbers = {
    'James': 7,
    'Thabo': 3,
    'Aisha': 11,
    'Zanele': 5,
    'Neo': 9
}

print("Favorite Numbers:")
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}")
print("\n")

# 6-3. Glossary
glossary = {
    'variable': 'A name used to store data in a program.',
    'loop': 'A way to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs.',
    'function': 'A reusable block of code that performs a specific task.',
    'string': 'A sequence of characters, used to represent text.'
}

print("Programming Glossary:")
for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")