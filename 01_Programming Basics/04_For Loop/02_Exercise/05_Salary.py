# "Facebook" -> 150 лв.
# "Instagram" -> 100 лв.
# "Reddit" -> 50 лв.
n = int(input())
salary = int(input())

salary_lost = False

for _ in range(n):
    current_site = input()
    if current_site == "Facebook":
        salary -= 150
    elif current_site == "Instagram":
        salary -= 100
    elif current_site == "Reddit":
        salary -= 50
    if salary <= 0:
        salary_lost = True
        break

if not salary_lost:
    print(salary)
else:
    print("You have lost your salary.")
