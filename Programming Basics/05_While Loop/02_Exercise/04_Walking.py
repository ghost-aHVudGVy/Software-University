current_input = input()
goal = 10000
total_steps = 0
goal_reached = False

while total_steps < goal:
    if current_input == "Going home":
        current_steps = int(input())
        total_steps += current_steps
        if total_steps >= goal:
            goal_reached = True
            break
        else:
            print(f"{goal - total_steps} more steps to reach goal.")
            break

    current_steps = int(current_input)
    total_steps += current_steps
    if total_steps >= goal:
        goal_reached = True
        break
    current_input = input()

if goal_reached:
    print("Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")
