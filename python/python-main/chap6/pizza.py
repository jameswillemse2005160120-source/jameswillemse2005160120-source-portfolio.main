pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }
# Summarize the order.
1 print(f"You ordered a {pizza['crust']}-crust pizza "
 "with the following toppings:")
2 for topping in pizza['toppings']:
 print(f"\t{topping}")

