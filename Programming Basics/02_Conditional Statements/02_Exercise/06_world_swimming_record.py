from functools import total_ordering

record = float(input())
distance = float(input())
time_1_m = float(input())

times_delay = distance // 15
delay = times_delay * 12.5
total_time = (distance * time_1_m) + delay

diff = abs(total_time - record)

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
