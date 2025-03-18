from math import trunc

hour = int(input())
minutes = int(input())

time_in_minutes = (hour * 60) + minutes + 15
real_hour = trunc(time_in_minutes / 60)
real_minutes = time_in_minutes % 60

if real_hour > 23:
    real_hour = 0

if real_minutes < 10:
    print(f"{real_hour}:0{real_minutes}")
else:
    print(f"{real_hour}:{real_minutes}")

# Second way:
# hours = int(input())
# minutes = int(input())
#
# minutes_plus_15 = minutes + 15
#
# if minutes_plus_15 >= 60:
#     minutes_plus_15 -= 60
#     hours += 1
#
# if hours >= 24:
#     hours -= 24
#
# if real_minutes < 10:
#     print(f"{hours}:{minutes_plus_15:02d}")
# else:
#     print(f"{hours}:{minutes_plus_15}")
