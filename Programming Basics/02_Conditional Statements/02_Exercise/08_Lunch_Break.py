from math import ceil

series = str(input())
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
chill_time = break_time / 4

free_time = break_time - (lunch_time + chill_time)

diff = abs(free_time - episode_time)

if free_time >= episode_time:
    print(f"You have enough time to watch {series} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(diff)} more minutes.")
