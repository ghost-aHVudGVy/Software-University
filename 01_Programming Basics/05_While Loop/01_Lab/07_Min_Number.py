from sys import maxsize

current_input = input()

min_num = maxsize

while current_input != "Stop":
    current_num = int(current_input)
    if current_num < min_num:
        min_num = current_num

    current_input = input()

print(min_num)
