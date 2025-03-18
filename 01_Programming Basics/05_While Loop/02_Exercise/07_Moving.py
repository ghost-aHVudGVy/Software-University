w = int(input())
l = int(input())
h = int(input())

free_space = w * l * h

current_input = input()
taken_space = 0
no_space = False

box_size = 1

while current_input != "Done":
    boxes = int(current_input)
    taken_space += boxes
    if taken_space >= free_space:
        no_space = True
        print(f"No more free space! You need {taken_space - free_space} Cubic meters more.")
        break
    current_input = input()

if not no_space:
    print(f"{free_space - taken_space} Cubic meters left.")
