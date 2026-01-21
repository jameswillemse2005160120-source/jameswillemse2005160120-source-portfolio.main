# Initial alien dictionary
alien_0 = {
    'color': 'green',
    'points': 5
}
print(alien_0)

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Movement logic based on speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':  # fixed typo from 'meduim'
    x_increment = 2
else:
    x_increment = 3  # ← Line 45, Col 5: colon added after `else`

# Update position
alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")

# Fixing malformed dictionary and deletion
alien_0 = {'color': 'green', 'points': 5}  # fixed keys and values
print(alien_0)

del alien_0['points']
print(alien_0)