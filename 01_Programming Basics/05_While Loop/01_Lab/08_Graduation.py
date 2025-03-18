name = input()

grade_count = 1
sum_grade = 0
bad_grade = 0

while grade_count <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_grade += 1
        if bad_grade > 1:
            print(f"{name} has been excluded at {grade_count} grade")
            break
        continue
    sum_grade += current_grade
    grade_count += 1
else:
    average_grade = sum_grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
