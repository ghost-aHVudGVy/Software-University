budget = int(input())
season = str(input())
people = int(input())

cost = 0

match season:
    case "Spring":
        cost = 3000
    case "Summer" | "Autumn":
        cost = 4200
    case "Winter":
        cost = 2600

if people <= 6:
    cost *= 0.9
elif people <= 11:
    cost *= 0.85
elif people >= 12:
    cost *= 0.75

if season != "Autumn" and people % 2 == 0:
    cost *= 0.95

is_enough = budget >= cost
diff = abs(budget - cost)

if is_enough:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
