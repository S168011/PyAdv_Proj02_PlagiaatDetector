fruits = ["appel", "peer", "banaan", "sinaasappel"]

enumerated_fruits = list(enumerate(fruits))

print(enumerated_fruits)

for fruit in enumerated_fruits:
    print(f"{fruit[0]}. {fruit[1]}")