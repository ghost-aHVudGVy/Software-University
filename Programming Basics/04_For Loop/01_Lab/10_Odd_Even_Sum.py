n = int(input())

odd_sum = 0
even_sum = 0

for num in range(n):
    current_num = int(input())
    if num % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

diff = abs(even_sum - odd_sum)
if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {diff}")
