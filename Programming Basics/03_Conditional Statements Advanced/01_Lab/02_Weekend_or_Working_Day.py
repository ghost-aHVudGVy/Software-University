day = str(input())

working_day = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
weekend_day = {"Saturday", "Sunday"}

if day in working_day:
    print("Working day")
elif day in weekend_day:
    print("Weekend")
else:
    print("Error")
