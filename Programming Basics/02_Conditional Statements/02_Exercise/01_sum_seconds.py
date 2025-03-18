from math import trunc

time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

sum_time = time_1 + time_2 + time_3

minutes = trunc(sum_time / 60)
seconds = sum_time % 60

if seconds < 10:
    print(f"{minutes}:{seconds:02d}")
else:
    print(f"{minutes}:{seconds}")
