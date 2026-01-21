alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
1 aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)

{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
1 for alien_number in range(30):
2 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
3 aliens.append(new_alien)
# Show the first 5 aliens.
4 for alien in aliens[:5]:
 print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
for alien in aliens[:3]:
 if alien['color'] == 'green':
 alien['color'] = 'yellow'
 alien['speed'] = 'medium'
 alien['points'] = 10
# Show the first 5 aliens.
for alien in aliens[:5]:
 print(alien)
print("...")

{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}


for alien in aliens[0:3]:
 if alien['color'] == 'green':
 alien['color'] = 'yellow'
 alien['speed'] = 'medium'
 alien['points'] = 10
 elif alien['color'] == 'yellow':
 alien['color'] = 'red'
 alien['speed'] = 'fast'
 alien['points'] = 15