current_input = input()

while current_input != "End":
    destination = current_input
    goal_money = float(input())
    saved_money = 0
    while saved_money < goal_money:
        current_money = float(input())
        saved_money += current_money

    print(f"Going to {destination}!")
    current_input = input()
