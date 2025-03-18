current_input = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while current_input != "stop":
    number = int(current_input)
    if number < 0:
        print("Number is negative.")
        current_input = input()
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers_sum += number
    else:
        non_prime_numbers_sum += number

    current_input = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
