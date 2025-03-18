start = int(input())
end = int(input())

buff = ""

for number in range(start, end + 1):
    even_sum = 0
    odd_sum = 0
    index = 0
    string_number = str(number)
    for index, digit in enumerate(string_number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
        index += 1
    if even_sum == odd_sum:
        print(number, end=" ")
