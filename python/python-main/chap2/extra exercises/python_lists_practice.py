# 3-8. Seeing the World
print("3-8. Seeing the World:")

places = ["Japan", "Norway", "New Zealand", "Brazil", "Iceland"]

# Original list
print("\nOriginal list:")
print(places)

# Alphabetical order with sorted()
print("\nAlphabetical (sorted):")
print(sorted(places))

# Original list remains unchanged
print("\nStill original:")
print(places)

# Reverse alphabetical order with sorted()
print("\nReverse alphabetical (sorted):")
print(sorted(places, reverse=True))

# Original list still unchanged
print("\nStill original:")
print(places)

# Reverse the list with reverse()
places.reverse()
print("\nReversed list:")
print(places)

# Reverse again to restore original order
places.reverse()
print("\nBack to original order:")
print(places)

# Sort the list alphabetically (modifies the list)
places.sort()
print("\nList sorted alphabetically:")
print(places)

# Sort in reverse alphabetical order
places.sort(reverse=True)
print("\nList sorted in reverse alphabetical order:")
print(places)

# 3-9. Dinner Guests
print("\n3-9. Dinner Guests:")
dinner_guests = ["Leonardo da Vinci", "Nikola Tesla"]
print(f"You are inviting {len(dinner_guests)} people to dinner.")

# 3-10. Every Function
print("\n3-10. Every Function:")

# List of countries
countries = ["Canada", "Germany", "Kenya", "Australia", "Sweden"]

# Print original list
print("\nOriginal list of countries:")
print(countries)

# Access by index
print("\nFirst country:", countries[0])
print("Last country:", countries[-1])

# Add a new country
countries.append("India")
print("\nAfter appending 'India':")
print(countries)

# Insert a country at position 2
countries.insert(2, "Brazil")
print("\nAfter inserting 'Brazil' at index 2:")
print(countries)

# Remove a country by value
countries.remove("Germany")
print("\nAfter removing 'Germany':")
print(countries)

# Delete an item by index
del countries[3]
print("\nAfter deleting item at index 3:")
print(countries)

# Pop last item
popped = countries.pop()
print(f"\nAfter popping last item ('{popped}'):")
print(countries)

# Pop specific item
popped_specific = countries.pop(1)
print(f"\nAfter popping index 1 ('{popped_specific}'):")
print(countries)

# Sort temporarily
print("\nSorted list temporarily:", sorted(countries))

# Sort permanently
countries.sort()
print("\nPermanently sorted list:")
print(countries)

# Reverse the list
countries.reverse()
print("\nReversed list:")
print(countries)

# Length of the list
print(f"\nNumber of countries in list: {len(countries)}")

