# List of sandwiches
sandwish_orders = ['tuna', 'beef', 'chicken', 'veggie', 'pork']

finished_sandwiches = []

while sandwish_orders:
    finished_sandwich = sandwish_orders.pop()
    
    print(f"\nI made you {finished_sandwich} sandwich!")
    finished_sandwiches.append(finished_sandwich)

print("\nThe following are the sandwiches made: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())    