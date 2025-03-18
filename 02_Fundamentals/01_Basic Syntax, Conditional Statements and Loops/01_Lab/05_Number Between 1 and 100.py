current_number = float(input())

while 1 > current_number or current_number > 100:
    current_number = float(input())
else:
    print(f"The number {current_number} is between 1 and 100")
