budget = float(input())
season = str(input())
destination = ""
money_spent = 0
type = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type = "Camp"
        money_spent = budget * 0.3
    elif season == "winter":
        type = "Hotel"
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type = "Camp"
        money_spent = budget * 0.4
    elif season == "winter":
        type = "Hotel"
        money_spent = budget * 0.80
else:
    destination = "Europe"
    type = "Hotel"
    money_spent = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type} - {money_spent:.2f}")
