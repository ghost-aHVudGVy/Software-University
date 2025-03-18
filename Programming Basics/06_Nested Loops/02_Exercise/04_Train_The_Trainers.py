judges_number = int(input())
current_input = input()
total_grades_sum = 0
grade_counter = 0
while current_input != "Finish":
    current_grades_sum = 0
    current_presentation = current_input
    for _ in range(judges_number):
        current_grade = float(input())
        current_grades_sum += current_grade
        grade_counter += 1

    average_grade = current_grades_sum / judges_number
    total_grades_sum += current_grades_sum
    print(f"{current_presentation} - {average_grade:.2f}.")
    current_input = input()

total_average_grade = total_grades_sum / grade_counter
print(f"Student's final assessment is {total_average_grade:.2f}.")
