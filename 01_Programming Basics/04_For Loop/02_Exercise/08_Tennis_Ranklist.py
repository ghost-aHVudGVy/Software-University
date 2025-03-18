from math import floor

num_tournament = int(input())
starting_points = int(input())

points_counter = 0
wins_counter = 0

for _ in range(num_tournament):
    current_input = input()
    if current_input == "W":
        points_counter += 2000
        wins_counter += 1
    elif current_input == "F":
        points_counter += 1200
    elif current_input == "SF":
        points_counter += 720

average = points_counter / num_tournament
win_rate = wins_counter / num_tournament * 100

print(f"Final points: {points_counter + starting_points}")
print(f"Average points: {floor(average)}")
print(f"{win_rate:.2f}%")
