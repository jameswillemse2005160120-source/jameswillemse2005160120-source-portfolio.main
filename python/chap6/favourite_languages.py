favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'erin': 'java'
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages:
    print(name.title())

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

friends = ['phil', 'sarah']

for  name in favourite_languages.key():
print("")
name  in friends:

new_position: 3
original_position: 0
new_position: 2
original_position: 0
new_position: 1


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

next line.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
1 language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
To see which language Sarah chose, we ask for the value at:
favorite_languages['sarah']

Sarah's favorite language is C.


 ~~~~~~~^^^^^^^^^^
KeyError: 'points'


 }

for key, value in user_0.items():
 print(f"\nKey: {key}")
 print(f"Value: {value}")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")

Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Rust.
Phil's favorite language is Python.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
for name in favorite_languages.keys():
 print(name.title())

favorite_languages = {
 --snip--
 }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 print(f"Hi {name.title()}.")
1 if name in friends:
2 language = favorite_languages[name].title()
 print(f"\t{name.title()}, I see you love {language}!")

favorite_languages = {
 --snip--
 }
if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())

favorite_languages = {
 --snip--
 }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
 print(language.title())

 languages = {'python', 'rust', 'python', 'c'}
 languages
{'rust', 'python', 'c'}



...



 }

favorite_languages = {
 'jen': ['python', 'rust'],
 'sarah': ['c'],
 'edward': ['rust', 'go'],
 'phil': ['python', 'haskell'],
 }
1 for name, languages in favorite_languages.items():
 print(f"\n{name.title()}'s favorite languages are:")
2 for language in languages:
 print(f"\t{language.title()}")

Jen's favorite languages are:
 Python
 Rust
Sarah's favorite languages are:
 C
Edward's favorite languages are:
 Rust
 Go
Phil's favorite languages are:
 Python
 Haskell


