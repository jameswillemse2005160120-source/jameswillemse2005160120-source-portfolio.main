# 3-4. Guest List
guests = ["Albert Einstein", "Marie Curie", "Ada Lovelace"]

# Invitation messages
print("3-4. Guest List:")
for guest in guests:
    print(f"Dear {guest}, I’d like to invite you to dinner.")

# 3-5. Changing Guest List
print("\n3-5. Changing Guest List:")
unavailable_guest = guests[1]
print(f"\nUnfortunately, {unavailable_guest} can’t make it to dinner.")

# Replace with a new guest
guests[1] = "Nikola Tesla"

# New invitations
for guest in guests:
    print(f"Dear {guest}, you’re still invited to dinner!")

# 3-6. More Guests
print("\n3-6. More Guests:")
print("Great news! I found a bigger dinner table.")

# Adding more guests
guests.insert(0, "Isaac Newton")              # Beginning
guests.insert(len(guests) // 2, "Katherine Johnson")  # Middle
guests.append("Alan Turing")                  # End

# New invitations
for guest in guests:
    print(f"Dear {guest}, you’re invited to dinner at my place!")

# 3-7. Shrinking Guest List
print("\n3-7. Shrinking Guest List:")
print("Unfortunately, the new dinner table won’t arrive in time. I can invite only two guests.")

# Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can’t invite you to dinner.")

# Final invitations
for guest in guests:
    print(f"{guest}, you’re still invited to dinner.")

# Empty the list
del guests[0]
del guests[0]

# Print final empty list
print("\nFinal guest list:", guests)
