from math import trunc

number_of_pages = int(input())
pages_for_one_hour = int(input())
number_of_days = int(input())

number_of_hours_needed = number_of_pages // pages_for_one_hour
number_of_days_needed = number_of_hours_needed / number_of_days

print(number_of_days_needed)
