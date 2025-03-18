bad_grades_limit = int(input())

exercise_counter = 0
grade_sum = 0
bad_grades_counter = 0
current_input = input()
exercise_name = ""

while current_input != "Enough":
    exercise_counter += 1
    exercise_name = current_input
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter >= bad_grades_limit:
            print(f"You need a break, {bad_grades_limit} poor grades.")
            break
    grade_sum += current_grade
    current_input = input()
else:
    average_grade = grade_sum / exercise_counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {exercise_counter}")
    print(f"Last problem: {exercise_name}")
