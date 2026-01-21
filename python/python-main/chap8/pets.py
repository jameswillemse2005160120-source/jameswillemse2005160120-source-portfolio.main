def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def two_describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Re-defining describe_pet with keyword arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Re-defining describe_pet again
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Final version with default argument
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Function calls (moved below all definitions)
describe_pet('willie')  # Uses default 'dog'
describe_pet(pet_name='willie')  # Uses default 'dog'
describe_pet('harry', 'hamster')  # Overrides default
describe_pet(pet_name='harry', animal_type='hamster')  # Keyword args
describe_pet(animal_type='hamster', pet_name='harry')  # Keyword args