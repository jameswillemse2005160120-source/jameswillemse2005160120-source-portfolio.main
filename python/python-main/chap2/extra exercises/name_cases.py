# Print a basic message
message = "Hi there Python World! I am James"
print(message)

# Personalized greeting
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

print("----- Exercise 2.4 -----")

# Store the user's name in a variable
name = "Eric"

# Print a message with the name in title case
print(f"Hello {name.title()}, would you like to learn some Python today?")

# Print a message with the name in lowercase
print(f"Hello {name.lower()}, would you like to learn some Python today?")

# Print a message with the name in uppercase
print(f"Hello {name.upper()}, would you like to learn some Python today?")

# Quote and attribution
quote = "‘Insanity is doing the same thing over and over again and expecting different results.’"
famous_person = "Albert Einstein"

print(f"{famous_person} once said, {quote}")
print(f"However, there’s no evidence at all that Einstein ever said it. {quote}")

# Whitespace and formatting
name1 = "Ricky"
print(f"\n\t{name1}\n\twent\n\toutside")

# Print name vertically
print(f"\n\tR\n\tI\n\tC\n\tK\n\tY")

# Strip whitespace
name1 = ' Ricky '
print(f"{name1.lstrip()}\n{name1.rstrip()}\n{name1.strip()}")

# Filename manipulation
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
