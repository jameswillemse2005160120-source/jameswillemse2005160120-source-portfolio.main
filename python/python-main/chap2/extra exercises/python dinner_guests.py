# 3-1. Names
print("3-1. Names:")
names = ["Alice", "Ben", "Cleo", "Daniel"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2. Greetings
print("\n3-2. Greetings:")
for name in names:
    print(f"Hello {name}, hope you're having a great day!")

# 3-3. Your Own List
print("\n3-3. Your Own List:")
transportation = ["Tesla Model S", "Harley-Davidson motorcycle", "Boeing 747", "Subaru Outback"]

print(f"I would like to own a {transportation[0]}.")
print(f"I would like to ride a {transportation[1]}.")
print(f"I would love to fly in a {transportation[2]}.")
print(f"I’d enjoy driving a {transportation[3]}.")

# 3-4. Guest List
print("3-4. Guest List:")
guest_list = ["Leonardo da Vinci", "Frida Kahlo", "Stephen Hawking"]

for guest in guest_list:
    print(f"Dear {guest}, I would be honored to invite you to dinner.")

# 3-5. Changing Guest List
print("\n3-5. Changing Guest List:")
unavailable_guest = guest_list[1]
print(f"\nUnfortunately, {unavailable_guest} can't make it to dinner.")

# Replace Frida Kahlo with Nikola Tesla
guest_list[1] = "Nikola Tesla"

print("\nUpdated invitations:")
for guest in guest_list:
    print(f"Dear {guest}, you’re still invited to dinner!")

# 3-6. More Guests
print("\n3-6. More Guests:")
print("Good news! I found a bigger dinner table!")

# Add new guests
guest_list.insert(0, "Maya Angelou")                    # Beginning
guest_list.insert(len(guest_list)//2, "Galileo Galilei")  # Middle
guest_list.append("Jane Austen")                        # End

print("\nNew invitations:")
for guest in guest_list:
    print(f"Dear {guest}, please join me for dinner at my place!")

# 3-7. Shrinking Guest List
print("\n3-7. Shrinking Guest List:")
print("Unfortunately, my new table won’t arrive in time — I can only invite two guests.")

# Remove guests until only two remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner this time.")

# Final two guests
print("\nStill invited:")
for guest in guest_list:
    print(f"{guest}, you’re still invited to dinner!")

# Empty the list
del guest_list[0]
del guest_list[0]

# Confirm the list is empty
print("\nFinal guest list (should be empty):", guest_list)

