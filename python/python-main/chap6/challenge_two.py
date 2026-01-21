# 6-1. Person
# Create a dictionary to store information about a person
person = {
    'first_name': 'Lerato',
    'last_name': 'Mokoena',
    'age': 18,
    'city': 'Johannesburg'
}

# Print each piece of information stored in the dictionary
print("📌 Person Information:")
print("First Name:", person['first_name'])
print("Last Name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])
print("\n")  # Adds a blank line for readability

# 6-2. Favorite Numbers
# Create a dictionary to store people's favorite numbers
favorite_numbers = {
    'James': 7,
    'Thabo': 3,
    'Aisha': 11,
    'Zanele': 5,
    'Neo': 9
}

# Print each person's name and their favorite number
print("🔢 Favorite Numbers:")
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}")
print("\n")

# 6-3. Glossary
# Create a glossary of programming terms
glossary = {
    'variable': 'A name used to store data in a program.',
    'loop': 'A way to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs.',
    'function': 'A reusable block of code that performs a specific task.',
    'string': 'A sequence of characters, used to represent text.'
}

# Print each word and its meaning with neat formatting
print("📘 Programming Glossary:")
for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")  # Newline between each pair