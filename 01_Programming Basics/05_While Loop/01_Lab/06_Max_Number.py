import sys

current_input = input()

max_number = -sys.maxsize

while current_input != "Stop":
    current_num = int(current_input)
    if current_num > max_number:
        max_number = current_num

    current_input = input()

print(max_number)
