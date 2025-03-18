trip_cost = float(input())
current_money = float(input())
spend_counter = 0
day_counter = 0
while current_money < trip_cost:
    day_counter += 1
    current_action = input()
    money = float(input())
    if current_action == "spend":
        spend_counter += 1
        if spend_counter == 5:
            print(f"You can't save the money.")
            print(f"{day_counter}")
            break
        current_money -= money
        if current_money <= 0:
            current_money = 0
    elif current_action == "save":
        spend_counter = 0
        current_money += money

if current_money >= trip_cost:
    print(f"You saved the money for {day_counter} days.")
