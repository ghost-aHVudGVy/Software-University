holiday_cost = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_toy_count = puzzles + dolls + bears + minions + trucks

money = (puzzles * 2.60) + (dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2)

if total_toy_count >= 50:
    money *= 0.75

money *= 0.9

diff = abs(money - holiday_cost)
if money >= holiday_cost:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
