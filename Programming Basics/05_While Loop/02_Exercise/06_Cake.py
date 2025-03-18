l = int(input())
w = int(input())

cake_area = l * w
peace = 1
peace_counter = 0
cake_finished = False

current_input = input()

while current_input != "STOP":
    current_pieces = int(current_input)
    peace_counter += current_pieces
    if peace_counter >= cake_area:
        cake_finished = True
        print(f"No more cake left! You need {peace_counter - cake_area} pieces more.")
        break
    current_input = input()

if not cake_finished:
    print(f"{cake_area - peace_counter} pieces are left.")
