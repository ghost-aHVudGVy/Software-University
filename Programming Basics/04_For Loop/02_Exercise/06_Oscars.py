actor_name = input()
academy_points = float(input())
judge_count = int(input())
nominee = False
for _ in range(judge_count):
    name_points = len(input())
    judge_points = float(input())
    academy_points += judge_points * name_points / 2
    if academy_points >= 1250.5:
        nominee = True
        break

diff = abs(academy_points - 1250.5)
if nominee:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
