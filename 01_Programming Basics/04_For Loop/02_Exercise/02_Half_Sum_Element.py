from sys import maxsize

n = int(input())

biggest_num = -maxsize
sum = 0

for num in range(n):
    number = int(input())
    if number > biggest_num:
        biggest_num = number
    sum += number

sum -= biggest_num
diff = abs(sum - biggest_num)
if sum == biggest_num:
    print(f"Yes")
    print(f"Sum = {sum}")
else:
    print(f"No")
    print(f"Diff = {diff}")
