def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
1 full_name = f"{first_name} {last_name}"
2 return full_name.title()
3 musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("Jimi Hendrix")
def get_formatted_name(first_name, middle_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {middle_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
def get_formatted_name(first_name, last_name, middle_name=''):
 """Return a full name, neatly formatted."""
1 if middle_name:
 full_name = f"{first_name} {middle_name} {last_name}"
2 else:
 full_name = f"{first_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
3 musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)