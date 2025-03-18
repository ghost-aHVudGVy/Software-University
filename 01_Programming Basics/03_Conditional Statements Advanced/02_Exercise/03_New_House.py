type = str(input())
quantity = int(input())
budget = int(input())

price = 0

if type == "Roses":
    price = quantity * 5
    if quantity > 80:
        price *= 0.9
elif type == "Dahlias":
    price = quantity * 3.80
    if quantity > 90:
        price *= 0.85
elif type == "Tulips":
    price = quantity * 2.80
    if quantity > 80:
        price *= 0.85
elif type == "Narcissus":
    price = quantity * 3
    if quantity < 120:
        price *= 1.15
elif type == "Gladiolus":
    price = quantity * 2.50
    if quantity < 80:
        price *= 1.20

is_enough = budget >= price
diff = abs(budget - price)

if is_enough:
    print(f"Hey, you have a great garden with {quantity} {type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
