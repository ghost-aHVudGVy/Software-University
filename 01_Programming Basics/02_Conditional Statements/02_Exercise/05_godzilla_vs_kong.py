budget = float(input())
people = int(input())
clothes_1 = float(input())

clothes = people * clothes_1
decor = budget * 0.1
if people > 150:
    clothes *= 0.9

total_cost = clothes + decor
diff = abs(budget - total_cost)

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
