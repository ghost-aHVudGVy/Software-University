n = int(input())

sum_first = 0
sum_second = 0

for i in range(2 * n):
    num = int(input())
    if i < n:
        sum_first += num
    else:
        sum_second += num

diff = abs(sum_first - sum_second)
if sum_first == sum_second:
    print(f"Yes, sum = {sum_first}")
else:
    print(f"No, diff = {diff}")
