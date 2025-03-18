current_input = input()

total_money = 0

while current_input != "NoMoreMoney":
    current_num = float(current_input)
    if current_num < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {current_num:.2f}")

    total_money += current_num
    current_input = input()

print(f"Total: {total_money:.2f}")
