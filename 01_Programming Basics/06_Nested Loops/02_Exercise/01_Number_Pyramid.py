number = int(input())

current_number = 0
goal_reached = False
for line in range(number):
    buff = ""
    for column in range(line + 1):
        current_number += 1
        buff += f"{current_number} "
        if current_number == number:
            goal_reached = True
            break

    print(buff)
    if goal_reached:
        break
