n = int(input())

start = 1111
end = 9999

for number in range(start, end + 1):
    is_special_number = False
    pass_counter = 0
    str_number = str(number)
    for index, digit in enumerate(str_number):
        current_digit = int(digit)
        if current_digit != 0 and n % current_digit == 0:
            pass_counter += 1
            if pass_counter == len(str_number):
                is_special_number = True
        else:
            break

    if is_special_number:
        print(number, end=" ")
