age = int(input())
washing_machine_price = float(input())
one_toy_price = int(input())

toy_count = 0
money_gift = 10
money = 0
brother_taking_money = 1

for current_age in range(1, age + 1):
    if current_age % 2 == 0:
        money += current_age * 10 / 2 - brother_taking_money
    else:
        toy_count += 1

toy_money = toy_count * one_toy_price
total_money = money + toy_money

diff = abs(total_money - washing_machine_price)
if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
